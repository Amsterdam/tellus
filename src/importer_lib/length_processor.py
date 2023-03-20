import logging

from datasets.tellus_data.models import LengteInterval
from importer_lib.parser import parse_length_interval

log = logging.getLogger(__name__)


def create_length_intervals(values):
    for index, value in enumerate(values):
        [min_cm, max_cm] = parse_length_interval(value)
        db_row, created = LengteInterval.objects.update_or_create(
            id=index + 1, label=value, min_cm=min_cm, max_cm=max_cm
        )
        if created:
            log.info("Created {}".format(str(db_row)))
        else:
            log.info("Updated {}".format(str(db_row)))
