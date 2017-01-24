import logging
import os
from functools import lru_cache

from swiftclient.client import Connection

# from io import BytesIO

log = logging.getLogger(__name__)

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("swiftclient").setLevel(logging.WARNING)

assert os.getenv('TELLUS_OBJECTSTORE_PASSWORD')

os_connect = {
    'auth_version': '2.0',
    'authurl': 'https://identity.stack.cloudvps.com/v2.0',
    'user': 'Tellus',
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
    page = []
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
    "splits of all but the last"
    return '_'.join(lst.split('_')[:-1])


def fetch_meta_data():
    """
    :return: return the xls file object
    """
    file_name = "AMS365_Codeboek.xlsx"
    folder = "meta"
    log.info("Fetch file {} in {}".format(file_name, folder))
    return get_conn().get_object("tellus", '{}/{}'.format(folder, file_name))[1]


def select_last_created_files(seq, key_func=split_prefix):
    """
    select the last file
    :param seq:
    :param key_func:
    :return:
    """
    my_files = [(key_func(c), c) for c in sorted(seq)]
    latest_in_group = {f[0]: f[1] for f in my_files}
    return sorted([k for c, k in latest_in_group.items()])


def fetch_last_tellus_data():
    files = []
    folder = 'data'
    for file_object in get_full_container_list("tellus", prefix=folder):
        if file_object['content_type'] != 'application/directory':
            path = file_object['name'].split('/')
            file_name = path[-1]
            files.append(file_name)
    file_name = files[-1]
    log.info("Fetch file {} in {}".format(file_name, folder))
    return get_conn().get_object("tellus", '{}/{}'.format(folder, file_name))[1]
