"""Import tellus csv's."""
import csv
import functools
import logging
import os
import time

import django
import openpyxl
import pytz
from dateutil.parser import parse as parse_date
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection

django.setup()

from importer_lib.parser import parse_speed_interval, parse_length_interval
from django.contrib.gis.geos import Point  # noqa

from datasets.tellus_data.models import SnelheidsInterval, Telling, SnelheidsCategorie  # noqa
from datasets.tellus_data.models import MeetraaiCategorie  # noqa
from datasets.tellus_data.models import RepresentatiefCategorie  # noqa
from datasets.tellus_data.models import ValidatieCategorie  # noqa
from datasets.tellus_data.models import LengteInterval  # noqa
from datasets.tellus_data.models import Meetlocatie  # noqa
from datasets.tellus_data.models import Tellus  # noqa
from datasets.tellus_data.models import TelRichting  # noqa

from objectstore.objectstore import fetch_meta_data, fetch_tellus_data_file_names  # noqa
from objectstore.objectstore import fetch_tellus_data_file_object  # noqa

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
def get_length_interval(id):
    return LengteInterval.objects.get(id=id)


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
            print(f"failure to convert string to id: {meetlocatie_str}")
            raise e

    return TelRichting.objects.get(
        richting=richting_id,
        tellus__meetlocatie__id=location_id
    )


def process_tel_richting(tellus, richting, naam, zijstraat):
    tel_richting, _ = TelRichting.objects.update_or_create(
        tellus=tellus,
        richting=richting,
        naam=naam,
        zijstraat=zijstraat
    )


def decodedata(filebytes):
    """
    The csv can be in UTF-8 or LATIN- 1, 2, or 3 depending on the producing
    machine.

    :param filebytes:
    :return: decoded string
    """
    encodings = ('UTF-8', 'LATIN-1', 'LATIN-2', 'LATIN-3')
    stringdata = None
    for encode in encodings:
        try:
            stringdata = filebytes.decode(encode)
            break
        except UnicodeDecodeError:
            pass
    if not stringdata:
        raise UnicodeDecodeError
    return stringdata


def insert_telling_batch(cursor, batch_list):
    args_str = ','.join(batch_list)
    cursor.execute("INSERT INTO tellus_data_telling " +
                   "(tel_richting_id, tijd_van, tijd_tot, aantal, lengte_interval_id, " +
                   "snelheids_interval_id, validatie_categorie_id," +
                   "meetraai_categorie_id, representatief_categorie_id" +
                   ") VALUES" + args_str)


class TellusImporter(object):

    def __init__(self, codebook, codebook_addon):
        self.codebook_sheets = self._import_meta(codebook)
        self.codebook_addon_sheets = self._import_meta(codebook_addon)

    def _import_meta(self, codebook_filename):
        """
        Function that retrieves the meta data from a Objectstore
        """
        os.makedirs("/tmp/tellus", exist_ok=True)
        with open("/tmp/tellus/{}".format(codebook_filename), 'wb') as f:
            f.write(fetch_meta_data(codebook_filename))

        wb = openpyxl.load_workbook("/tmp/tellus/{}".format(codebook_filename))
        return {sheet_name: wb[sheet_name] for
                sheet_name in wb.sheetnames}

    def process_tellus_locaties(self, title_row=1,
                                first_col=0):
        """
        Import the data for the Tellus (Locations)
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        for row in self.codebook_addon_sheets['Locaties'].iter_rows(
                min_row=title_row + 1,
                min_col=first_col):
            res = [cell.value for cell in row]

            if not res[0]:
                # ignore empty rows
                continue

            # Meetlocatie
            meetlocatie, _ = Meetlocatie.objects.update_or_create(
                id=res[12],
                name=res[2]
            )

            # Tellus
            objnr_vor=res[0]  # e.g.: TP0001
            tellus_id = int(objnr_vor[2:])  # e.g.: 1

            tellus, _ = Tellus.objects.update_or_create(
                id=tellus_id,
                objnr_vor=objnr_vor,
                objnr_leverancier=res[1],
                snelheids_categorie=res[11],
                latitude=res[9],
                longitude=res[10],
                rijksdriehoek_x=res[7],
                rijksdriehoek_y=res[8],
                geometrie=Point(float(res[7]), float(res[8]), srid=28992),
                meetlocatie=meetlocatie
            )

            # TelRichting
            if res[5] != 'n.v.t.':  # Richting 1
                process_tel_richting(tellus, 1, res[5], res[3])
            if res[6] != 'n.v.t.':  # Richting 2
                process_tel_richting(tellus, 2, res[6], res[4])

            log.debug("Processed {}".format(str(res[0])))

    def process_snelheids_categorie(self, sheet_name='Snelheidscategorieen', title_row=1, first_col=1):
        """
        Import SnelheidsCategorie & SnelheidsInterval objects
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        EMPTY_CELL = 'nvt'
        for row in self.codebook_sheets[sheet_name].iter_rows(
                min_row=title_row + 1,
                max_row=5,
                min_col=first_col):
            res = [cell.value for cell in row]  # [1, '< 30 km/u', '31 - 40 km/u', ..., '> 100 km/u']
            categorie = int(res[0])             # 1
            values = res[1:]                    # ['< 30 km/u', '31 - 40 km/u', ..., '> 100 km/u']

            # Identify all unique intervals:
            for (index, interval_str) in enumerate(values):
                if interval_str == EMPTY_CELL:
                    continue
                [speed_min, speed_max] = parse_speed_interval(interval_str)
                db_row, created = SnelheidsInterval.objects.update_or_create(
                    label=interval_str,
                    min_kmph=speed_min,
                    max_kmph=speed_max
                )

                if created:
                    log.info("SnelheidsInterval created {}".format(str(db_row)))
                else:
                    log.info("SnelheidsInterval updated {}".format(str(db_row)))

            # Store reference from "Snelheid categorie" to interval.
            for (index, interval_str) in enumerate(values):
                if interval_str == EMPTY_CELL:
                    continue
                try:
                    interval = SnelheidsInterval.objects.get(label=interval_str)
                except ObjectDoesNotExist as e:
                    print(f"SnelheidsInterval not found for {interval_str}")
                    raise e
                db_row, created = SnelheidsCategorie.objects.update_or_create(
                    index=index + 1,    # called s1, s2, etc in source documents
                    categorie=categorie,
                    interval=interval
                )
                if created:
                    log.info("SnelheidsCategorie created {}".format(str(db_row)))
                else:
                    log.info("SnelheidsCategorie updated {}".format(str(db_row)))

    def process_meetraai_categorie(self):
        for row in self.codebook_sheets['Meetraai'].iter_rows(
                min_row=1, max_row=3, min_col=1):
            res = [cell.value for cell in row]
            db_row, created = MeetraaiCategorie.objects.update_or_create(
                id=res[0],
                label=res[1]
            )
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def process_representatief_categorie(self):
        for row in self.codebook_sheets['Representatief'].iter_rows(
                min_row=1, max_row=6, min_col=1):
            res = [cell.value for cell in row]
            db_row, created = RepresentatiefCategorie.objects.update_or_create(
                id=res[0],
                label=res[1])
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def process_validatie_categorie(self):
        for row in self.codebook_sheets['Validatie'].iter_rows(
                min_row=1, max_row=6, min_col=1):
            res = [cell.value for cell in row]
            db_row, created = ValidatieCategorie.objects.update_or_create(
                id=res[0],
                label=res[1])
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def process_lengte_interval(self, sheet_name='Lengtecategorieen', title_row=1, first_col=1):
        """
        Import LengteInterval objects
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        for row in self.codebook_sheets[sheet_name].iter_rows(
                min_row=title_row + 1,
                max_row=2,
                min_col=first_col):

            res = [cell.value for cell in row]  # [1, '0 - 5,1 m', ..., '> 12,2 m']
            values = res[1:]  # ['0 - 5,1 m', ..., '> 12,2 m']

            for (index, value) in enumerate(values):
                [min_cm, max_cm] = parse_length_interval(value)
                db_row, created = LengteInterval.objects.update_or_create(
                    id=index + 1,
                    label=value,
                    min_cm=min_cm,
                    max_cm=max_cm
                )
                if created:
                    log.info("Created {}".format(str(db_row)))
                else:
                    log.info("Updated {}".format(str(db_row)))

    def download_tellus_data(self, obj_store_path):
        filename = os.path.basename(obj_store_path)
        target_path = os.path.join('/tmp/tellus/', filename)
        exists = os.path.isfile(target_path)
        if exists:
            print("File exists, skipping download: {}".format(obj_store_path))
        else:
            with open(target_path, 'wb') as f:
                f.write(fetch_tellus_data_file_object(obj_store_path))
        return target_path

    def process_tellingen(self, csv_file_path):
        t0 = time.time()

        skipped_row_cnt = 0

        # Insertion into database is done in batches for performance reasons
        batch_idx = 0
        batch_insert_count = 2000
        batch_list = [None] * batch_insert_count  # preallocate array

        range60 = list(range(0, 60))

        with connection.cursor() as cursor:
            with open(csv_file_path) as csv_file:
                csvReader = csv.reader(csv_file, dialect='excel', delimiter=';')
                next(csvReader, None)
                row_cnt = 0
                item_cnt = 0
                for trow in csvReader:
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
                        log.debug(f"TelRichting not found for : {trow[0]}, {trow[1]}, skipping")
                        skipped_row_cnt += 1
                        continue
                    except Exception as e:
                        log.debug(f"Error querying database: {trow[0]}, {trow[1]}")
                        raise e

                    snelheids_categorie = tel_richting.tellus.snelheids_categorie

                    for idx in range60:
                        count_idx = 8 + idx  # Index of L1S1 cell + idx
                        speed_id = idx % 10 + 1  # Run from S1 to S10
                        length_id = int(idx / 10) + 1  # Run from L1 to L6

                        snelheids_interval_id = get_speed_interval_id(snelheids_categorie, speed_id)
                        lengte_interval = get_length_interval(length_id)
                        aantal = int(trow[count_idx])
                        query = f"({tel_richting.id},'{tijd_van}','{tijd_tot}',{aantal}," \
                                f"{lengte_interval.id},{snelheids_interval_id},{validatie_category.id}," \
                                f"{meetraai_category.id},{representatief_category.id})"
                        batch_list[batch_idx] = query

                        batch_idx += 1
                        if not batch_idx % batch_insert_count:  # TODO don't forget insert last few
                            insert_telling_batch(cursor, batch_list)
                            item_cnt += batch_insert_count

                            difference = time.time() - t0  # in seconds
                            log.debug(f"Import count: "
                                      f"{str(item_cnt)}items, "
                                      f"elapsed {int(difference)}s, "
                                      f"speed: {item_cnt / difference} items/s")
                            batch_idx = 0

                    row_cnt += 1

                # Insert last (partial) batch
                insert_telling_batch(cursor, batch_list[:batch_idx])


if __name__ == "__main__":
    assert os.getenv('TELLUS_OBJECTSTORE_PASSWORD')

    os.makedirs('/tmp/tellus', exist_ok=True)
    importer = TellusImporter(
        codebook='AMS365_codeboek_v5.xlsx',
        codebook_addon='AMS365_codeboek_v8_aanvulling.xlsx'
    )
    importer.process_meetraai_categorie()
    importer.process_representatief_categorie()
    importer.process_validatie_categorie()
    importer.process_lengte_interval()
    importer.process_snelheids_categorie()
    importer.process_tellus_locaties()

    log.debug("Delete all telling objects: ")
    Telling.objects.all().delete()
    log.debug("Delete telling objects done")

    for file_name in fetch_tellus_data_file_names():
        data_path = importer.download_tellus_data(file_name)
        print(data_path)
        importer.process_tellingen(data_path)

    log.info("Done importing tellus data")
