import os
from unittest import TestCase
from unittest import mock
from importer import TellusImporter
from objectstore.objectstore import fetch_meta_data


def mocked_fetch_meta_data(filename):
    import ipdb;
    ipdb.set_trace()
    filepath = os.path.dirname(os.path.abspath(__file__))
    r = open(f"{filepath}/fixture_files/{filename}").read()
    return r


class TestImport(TestCase):
    def setUp(self):
        os.putenv('TELLUS_OBJECTSTORE_PASSWORD', 'insecure')
        self.my_importer = None

    def test_import_meta(self):
        with mock.patch('objectstore.objectstore.fetch_meta_data', spec=mocked_fetch_meta_data) as patcher:
            print(patcher)
            fetch_meta_data("metadata.xlsx")
            # self.my_importer = TellusImporter(codebook_name="metadata.xlsx")
            assert len(self.my_importer.sheets) == 5

    def test_import(self):
        assert True
