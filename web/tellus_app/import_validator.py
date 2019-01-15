import logging

import django

django.setup()

from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from datasets.tellus_data.models import Tellus, SnelheidsInterval, LengteInterval, TellingCarsPerHourPerDay, \
    TellingCarsPerHourLength, TellingCarsPerHourSpeed, TellingCarsYMH, TellingCarsYMHLength, TellingCarsYMHSpeed, \
    Telling

log = logging.getLogger(__name__)

OBJSTORE_METADATA = 'meta'

functional_errors = []


def assert_count(minimal, actual, message):
    if actual < minimal:
        raise Exception("Import failed. {} minimal {}, actual {}".format(message, minimal, actual))


def log_leaf_migrations():
    """
    Log migration graph leaf nodes the current migration state can be derived from the logs.
    """
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    log.info('Leaf migrations')
    log.info(targets)


def check_import():
    log.info('Checking import')
    log.info('Checking database count')

    assert_count(30, Tellus.objects.count(), 'Tellus count')
    assert_count(20, SnelheidsInterval.objects.count(), 'SnelheidsInterval count')
    assert_count(6, LengteInterval.objects.count(), 'LengteInterval count')

    # TODO: bump expected count up when including all files again
    # assert_count(50 * 1000 * 1000, Telling.objects.count(), 'Tellingen count')
    # assert_count(40 * 1000 * 1000, Telling.objects.count(), 'Tellingen count')
    assert_count(1 * 1000 * 1000, Telling.objects.count(), 'Tellingen count')

    log_leaf_migrations()

    log.info("Checking materialized views: ")
    # assert_count(720 * 1000, TellingCarsPerHourPerDay.objects.count(), 'TellingCarsPerHourPerDay count')
    assert_count(1000, TellingCarsPerHourPerDay.objects.count(), 'TellingCarsPerHourPerDay count')
    # assert_count(4 * 1000 * 1000, TellingCarsPerHourLength.objects.count(), 'TellingCarsPerHourLength count')
    assert_count(1000, TellingCarsPerHourLength.objects.count(), 'TellingCarsPerHourLength count')
    # assert_count(7 * 1000 * 1000, TellingCarsPerHourSpeed.objects.count(), 'TellingCarsPerHourSpeed count')
    assert_count(1000, TellingCarsPerHourSpeed.objects.count(), 'TellingCarsPerHourSpeed count')
    # assert_count(45 * 1000, TellingCarsYMH.objects.count(), 'TellingCarsYMH count')
    assert_count(1000, TellingCarsYMH.objects.count(), 'TellingCarsYMH count')
    # assert_count(250 * 1000, TellingCarsYMHLength.objects.count(), 'TellingCarsYMHLength count')
    assert_count(1000, TellingCarsYMHLength.objects.count(), 'TellingCarsYMHLength count')
    # assert_count(450 * 1000, TellingCarsYMHSpeed.objects.count(), 'TellingCarsYMHSpeed count')
    assert_count(1000, TellingCarsYMHSpeed.objects.count(), 'TellingCarsYMHSpeed count')
    log.info("Materialized views checked")

    log.info('Check done')


if __name__ == "__main__":
    log.info("Check import")
    check_import()
    log.info("Check import done")
