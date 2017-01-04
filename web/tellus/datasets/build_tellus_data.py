from django.conf import settings
import psycopg2
from objectstore.objectstore import get_flobj_from_objectstore

OBJSTORE_TELLING = 'telling'

SQL_STATEMENT = """
    COPY %s FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS ';'
    """

class TellusData:
    def __init__(self):
        self.host = settings.DATABASES['default']['HOST']
        self.dbname = settings.DATABASES['default']['NAME']
        self.user = settings.DATABASES['default']['USER']
        self.password = settings.DATABASES['default']['PASSWORD']
        self.port = settings.DATABASES['default']['PORT']
        self.conn = psycopg2.connect("host={} port={} dbname={} user={}  password={}".format(
            self.host, self.port, self.dbname, self.user, self.password))

    def get_data(self):
        """
        Retrieve file like object from object store
        :return: file like object
        """
        return get_flobj_from_objectstore(OBJSTORE_TELLING)

    def load_data(self, table_name: str, file_object):

        cursor = self.conn.cursor()
        cursor.copy_expert(sql=SQL_STATEMENT % table_name, file=file_object)
        self.conn.commit()
        cursor.close()

    def decodedata(self, filebytes: bytes) -> str:
        """
        The csv can be in UTF-8 or LATIN- 1, 2, or 3 depending on the producing
        machine.

        :param filebytes:
        :return: decoded string
        """
        encodings = ('UTF-8', 'LATIN-1', 'LATIN-2', 'LATIN-3')
        stringdata = None
        for encode in encodings:
            try:
                stringdata = filebytes.decode(encode)
                break
            except UnicodeDecodeError:
                pass
        if not stringdata:
            raise UnicodeDecodeError
        return stringdata
