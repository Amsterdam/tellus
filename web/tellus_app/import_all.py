import logging
import multiprocessing
import os
import subprocess
from multiprocessing.pool import ThreadPool

from import_single import import_single
from importer import import_core, prepare_import_tellingen, get_tellingen_count, refresh_materialized_views

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
DO_PARALLEL = True


def import_tellingen_serial(csv_paths):
    for csv_path in csv_paths:
        import_single(csv_path)


def import_tellingen_job(csv_path):
    command = ["python", os.path.join(DIRECTORY, "import_single.py"), csv_path]
    logging.info(f"starting job: {command}")
    p = subprocess.Popen(command)
    p.wait()


def import_tellingen_parallel(csv_paths):
    cpu_count = multiprocessing.cpu_count()
    pool_size = int(cpu_count)
    logging.info(f"pool size: {pool_size}")
    tp = ThreadPool(pool_size)

    for csv_path in csv_paths:
        tp.apply_async(import_tellingen_job, (csv_path,))

    tp.close()
    tp.join()


def import_all():
    import_core()
    csv_paths = prepare_import_tellingen()

    if DO_PARALLEL:
        import_tellingen_parallel(csv_paths)
    else:
        import_tellingen_serial(csv_paths)

    logging.info("Done importing tellus data")
    logging.info(f"{get_tellingen_count()} tellingen")

    logging.info(f'Refreshing materialized views')
    refresh_materialized_views()
    logging.info(f'Refreshing views done')


if __name__ == "__main__":
    import_all()
