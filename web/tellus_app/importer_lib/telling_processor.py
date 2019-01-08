import atexit
import logging

import pytz
import functools
import time

from dateutil.parser import parse as parse_date
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from psycopg2.extras import execute_values

from datasets.tellus_data.models import SnelheidsCategorie
from datasets.tellus_data.models import MeetraaiCategorie
from datasets.tellus_data.models import RepresentatiefCategorie
from datasets.tellus_data.models import ValidatieCategorie
from datasets.tellus_data.models import LengteInterval
from datasets.tellus_data.models import TelRichting

log = logging.getLogger(__name__)


def memoize(func):
    """
    Wraps (pure) function so results are cached per input
    """
    cache = func.cache = {}

    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return memoized_func


@memoize
def get_speed_interval_id(categorie, id):
    return SnelheidsCategorie.objects.get(categorie=categorie, index=id).interval_id


@memoize
def get_length_interval_id(id):
    return LengteInterval.objects.get(id=id).id


@memoize
def get_validation_category(id):
    return ValidatieCategorie.objects.get(id=id)


@memoize
def get_meetraai_category(id):
    return MeetraaiCategorie.objects.get(id=id)


@memoize
def get_representatief_category(id):
    return RepresentatiefCategorie.objects.get(id=id)


@memoize
def get_tel_richting(meetlocatie_str, richting_id):
    # meetlocatie_str, e.g.: 2, T02 or T12+13
    try:
        # case meetlocatie_str is integer
        location_id = int(meetlocatie_str)
    except ValueError:
        # Case where meetlocatie_str must first be unpacked
        # T02 -> 2
        # T12+13 -> 12
        try:
            location_id = int(meetlocatie_str[1:3])
        except Exception as e:
            log.error(f"failure to convert string to id: {meetlocatie_str}")
            raise e

    return TelRichting.objects.get(
        richting=richting_id,
        tellus__meetlocatie__id=location_id
    )


def clear_memoize_caches():
    """
    Clears any caches created by memoize, required before exiting because django/contrib/gis will throw an error if
    program exits while a Gis object is still in memory.
    Related to: https://github.com/django/django/pull/10130, but not solved by Django 2.1.3
    """
    get_speed_interval_id.cache.clear()
    get_length_interval_id.cache.clear()
    get_validation_category.cache.clear()
    get_meetraai_category.cache.clear()
    get_representatief_category.cache.clear()
    get_tel_richting.cache.clear()


# Set function to be executed on normal program exit
atexit.register(clear_memoize_caches)


def insert_telling_batch(cursor, values_list):
    insertQuery = """
INSERT INTO tellus_data_telling 
(tel_richting_id, tijd_van, tijd_tot, aantal, lengte_interval_id, 
snelheids_interval_id, validatie_categorie_id,
meetraai_categorie_id, representatief_categorie_id)
VALUES %s
"""
    execute_values(cursor, insertQuery, values_list)


def process_telling_sheet(file_name, csv_reader):
    t0 = time.time()

    skipped_row_cnt = 0

    # Insertion into database is done in batches for performance reasons
    batch_idx = 0
    batch_insert_count = 2000
    batch_list = [None] * batch_insert_count  # preallocate array

    range60 = list(range(0, 60))
    with connection.cursor() as cursor:
        next(csv_reader, None)
        row_cnt = 0
        item_cnt = 0

        for trow in csv_reader:
            if not trow[0]:
                log.debug('Ignoring empty row.')
                continue

            tijd_van = parse_date(trow[6]).replace(tzinfo=pytz.UTC)
            tijd_tot = parse_date(trow[7]).replace(tzinfo=pytz.UTC)
            validatie_category = get_validation_category(trow[2])
            representatief_category = get_representatief_category(trow[3])
            meetraai_category = get_meetraai_category(trow[4])

            try:
                tel_richting = get_tel_richting(trow[0], trow[1])
            except ObjectDoesNotExist:
                # Source file should describe all "tellussen" for both directions,
                # but sometimes a direction is missing in the tellus description file.
                # Even though, there are actual counts for this direction.
                # e.g.: T32 direction 2 is sometimes measured, even though
                # there is no reference to it.
                # T32 is measuring a one way street. So any counts in the opposite direction are
                # illogical and we'll skip them during this import.
                log.info(f"TelRichting not found for : {trow[0]}, {trow[1]}, skipping")
                skipped_row_cnt += 1
                continue
            except Exception as e:
                log.error(f"Error querying database for telRichting: meetlocatie {trow[0]}, richting {trow[1]}")
                raise e

            snelheids_categorie = tel_richting.tellus.snelheids_categorie

            for idx in range60:
                count_idx = 8 + idx  # Index of L1S1 cell + idx
                speed_id = idx % 10 + 1  # Run from S1 to S10
                length_id = int(idx / 10) + 1  # Run from L1 to L6

                snelheids_interval_id = get_speed_interval_id(snelheids_categorie, speed_id)
                lengte_interval_id = get_length_interval_id(length_id)
                aantal = int(trow[count_idx])
                values = (tel_richting.id,tijd_van,tijd_tot,aantal,
                        lengte_interval_id,snelheids_interval_id,validatie_category.id,
                        meetraai_category.id,representatief_category.id)
                batch_list[batch_idx] = values

                batch_idx += 1
                if not batch_idx % batch_insert_count:
                    insert_telling_batch(cursor, batch_list)
                    item_cnt += batch_insert_count

                    difference = time.time() - t0  # in seconds
                    log.debug(f"{file_name[-10:]}, Import count: "
                              f"{str(item_cnt)}items, "
                              f"elapsed {int(difference)}s, "
                              f"speed: {item_cnt / difference} items/s")
                    batch_idx = 0

            row_cnt += 1

        if batch_idx > 0:
            # Insert remaining (partial) batch
            insert_telling_batch(cursor, batch_list[:batch_idx])

    clear_memoize_caches()
