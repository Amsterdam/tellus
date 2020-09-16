import logging
import os
import sys

import django

django.setup()

from importer_lib.importer import import_telling


def import_single(csv_path):
    """
    Import tellingen in a single csv file
    """
    filename = os.path.basename(csv_path)
    logging.basicConfig(level=logging.INFO, format=f"Foo{filename[-20:]} %(message)s")

    logging.info(f"importing {csv_path}")
    import_telling(csv_path)
    logging.info(f"done importing {csv_path}")


if __name__ == "__main__":
    assert len(sys.argv) == 2
    import_single(sys.argv[1])
