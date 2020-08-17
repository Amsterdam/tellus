import logging

import django
from django.db import connection

django.setup()

from django.db.migrations.executor import MigrationExecutor  # noqa
from datasets.tellus_data.models import (
    Tellus,
    SnelheidsInterval,
    LengteInterval,
    Telling,
)  # noqa

log = logging.getLogger(__name__)

OBJSTORE_METADATA = "meta"

functional_errors = []


def assert_count(minimal, actual, message):
    if actual < minimal:
        raise Exception(
            "Import failed. {} minimal {}, actual {}".format(message, minimal, actual)
        )


def log_leaf_migrations():
    """
    Log migration graph leaf nodes so the current migration state can read from the logs.
    """
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    log.info("Leaf migrations")
    log.info(targets)


def check_import():
    log.info("Checking import")
    log.info("Checking database count")

    assert_count(30, Tellus.objects.count(), "Tellus count")
    assert_count(20, SnelheidsInterval.objects.count(), "SnelheidsInterval count")
    assert_count(6, LengteInterval.objects.count(), "LengteInterval count")
    assert_count(65 * 1000 * 1000, Telling.objects.count(), "Tellingen count")

    log_leaf_migrations()

    log.info("Check done")


if __name__ == "__main__":
    log.info("Check import")
    check_import()
    log.info("Check import done")
