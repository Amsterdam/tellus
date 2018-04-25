import logging
import os
from functools import lru_cache

from swiftclient.client import Connection

log = logging.getLogger(__name__)

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("swiftclient").setLevel(logging.WARNING)

os_connect = {
    'auth_version': '2.0',
    'authurl': 'https://identity.stack.cloudvps.com/v2.0',
    'user': 'tellus',
    'key': os.getenv('TELLUS_OBJECTSTORE_PASSWORD', 'insecure'),
    'tenant_name': 'BGE000081_Tellus',
    'os_options': {
        'tenant_id': '7aebee82a6c848ae847ad5084e385fec',
        'region_name': 'NL',
        # 'endpoint_type': 'internalURL'
    }
}


@lru_cache(maxsize=None)
def get_conn():
    assert os.getenv('TELLUS_OBJECTSTORE_PASSWORD')
    return Connection(**os_connect)


def get_full_container_list(container_name, **kwargs):
    """
    Return a listing of filenames in container `container_name`
    :param container_name:
    :param kwargs:
    :return:
    """
    limit = 10000
    kwargs['limit'] = limit
    seed = []
    _, page = get_conn().get_container(container_name, **kwargs)
    seed.extend(page)

    while len(page) == limit:
        # keep getting pages..
        kwargs['marker'] = seed[-1]['name']
        _, page = get_conn().get_container(container_name, **kwargs)
        seed.extend(page)
    return seed


def split_prefix(lst):
    """
    splits of all but the last
    """
    return '_'.join(lst.split('_')[:-1])


def fetch_meta_data(file_name="AMS365_codeboek_v7.xlsx"):
    """
    :return: return the xls file object
    """
    folder = "meta"
    log.info("Fetch file {} in {}".format(file_name, folder))
    return get_conn().get_object("tellus", '{}/{}'.format(folder, file_name))[1]


def fetch_tellus_data_file_object(file_name):
    log.info("Fetch file {}".format(file_name))
    return get_conn().get_object("tellus", file_name)[1]


def fetch_tellus_data_file_names():
    files = []
    folder = 'data'
    for file_object in get_full_container_list("tellus", prefix=folder):
        if file_object['content_type'] != 'application/directory':
            log.info("Found file {}".format(file_object['name']))
            files.append(file_object['name'])
    return files
