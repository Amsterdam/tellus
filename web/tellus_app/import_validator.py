import logging

import django

django.setup()

from datasets.tellus_data.models import (Tellus,
                                         SnelheidsInterval,
                                         LengteInterval,
                                         Telling
                                         )  # noqa

log = logging.getLogger(__name__)

OBJSTORE_METADATA = 'meta'

functional_errors = []


def assert_count(minimal, actual, message):
    if actual < minimal:
        raise Exception("Import failed. {} minimal {}, actual {}".format(message, minimal, actual))


def check_import():
    log.info('Checking import')
    log.info('Checking database count')

    assert_count(30, Tellus.objects.count(), 'Tellus count')
    assert_count(20, SnelheidsInterval.objects.count(), 'SnelheidsInterval count')
    assert_count(6, LengteInterval.objects.count(), 'LengteInterval count')

    # TODO: bump expected count up when including 2016 file again
    # assert_count(50 * 1000 * 1000, Telling.objects.count(), 'Tellingen count')
    assert_count(40 * 1000 * 1000, Telling.objects.count(), 'Tellingen count')

    log.info('Check done')


if __name__ == "__main__":
    log.info("Check import")
    check_import()
    log.info("Check import done")
