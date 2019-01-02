import logging
from django.core.exceptions import ObjectDoesNotExist
from datasets.tellus_data.models import SnelheidsInterval, SnelheidsCategorie
from importer_lib.parser import parse_speed_interval

EMPTY_CELL = 'nvt'

log = logging.getLogger(__name__)


def create_speed_intervals(interval_strs):
    for (index, interval_str) in enumerate(interval_strs):
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


def create_speed_category(categorie, interval_strs):
    for (index, interval_str) in enumerate(interval_strs):
        if interval_str == EMPTY_CELL:
            continue
        try:
            interval = SnelheidsInterval.objects.get(label=interval_str)
        except ObjectDoesNotExist as e:
            print(f"SnelheidsInterval not found for {interval_str}")
            raise e
        db_row, created = SnelheidsCategorie.objects.update_or_create(
            index=index + 1,  # called s1, s2, etc in source documents
            categorie=categorie,
            interval=interval
        )
        if created:
            log.info("SnelheidsCategorie created {}".format(str(db_row)))
        else:
            log.info("SnelheidsCategorie updated {}".format(str(db_row)))
