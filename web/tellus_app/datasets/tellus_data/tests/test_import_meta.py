from django.test import TestCase
from unittest.mock import patch
import datasets.tellus_data
from datasets.build_meta_data import MetaImporter


class TellusImportTest(TestCase):

    def setUp(self):
        pass

    def test_read_objectstore(self):
        t = MetaImporter()
        t.ImportMeta()

def _fixtures_meta_get():
    return open('tests/fixture_files/metadata.xlsx')


def _fixtures_telling_get():
    return open('tests/fixture_files/AMS365_2016-10.csv')


def patch_get_meta_from_objectstore(function):
    return patch('get_data', _fixtures_meta_get)(function)


def patch_get_telling_from_objectstore(function):
    return patch('get_files_from_objectstore', _fixtures_telling_get)(function)


# @patch_get_meta_from_objectstore
def test_import_meta():
    t = MetaImporter()
