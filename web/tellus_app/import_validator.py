import logging

import django

django.setup()

from datasets.tellus_data.models import (Tellus, SnelheidsCategorie,
                                         LengteCategorie, TellusData)  # noqa

log = logging.getLogger(__name__)

OBJSTORE_METADATA = 'meta'

functional_errors = []


def assert_count(minimal, actual, message):
    if actual < minimal:
        raise Exception("Import failed. {} minimal {}, actual {}".format(message, minimal, actual))


def check_import():
    log.info('Checking import')
    log.info('Checking database count')

    assert_count(20, Tellus.objects.count(), 'Tellus count')
    assert_count(300000, TellusData.objects.count(), 'TellusData count')
    assert_count(4, SnelheidsCategorie.objects.count(), 'SnelheidsCategorie count')
    assert_count(1, LengteCategorie.objects.count(), 'SnelheidsCategorie count')

    log.info('Check done')


if __name__ == "__main__":

    log.info("Check import")
    check_import()
    log.info("Check import done")
