import os
from unittest import TestCase
from unittest import mock

import openpyxl

from datasets.tellus_data.models import Tellus, SnelheidsCategorie, TellusData
from importer import TellusImporter


class TestImport(TestCase):
    @mock.patch('importer.TellusImporter._import_meta')
    def setUp(self, patched_import_meta):
        os.putenv('TELLUS_OBJECTSTORE_PASSWORD', 'insecure')
        assert patched_import_meta == TellusImporter._import_meta

        def _import_meta(self):
            filepath = os.path.dirname(os.path.abspath(__file__))
            wb = openpyxl.load_workbook(
                "{}/fixture_files/{}".format(filepath, self.codebook_name))
            self.sheets = {sheet_name: wb.get_sheet_by_name(sheet_name) for
                           sheet_name in wb.get_sheet_names()}

        # patch `_import_meta`
        TellusImporter._import_meta = _import_meta
        self.my_importer = TellusImporter(codebook_name="metadata.xlsx")

    def test_import_meta(self):
        # check if _import_meta has loaded XLS file
        assert len(self.my_importer.sheets) == 7

    def test_process_tellus_import(self):
        self.my_importer.process_lengte_categorie()
        self.my_importer.process_snelheids_categorie()
        assert SnelheidsCategorie.objects.count() == 4
        # import the `tellus_locaties`
        self.my_importer.process_tellus_locaties()

        # count the number of rows imported in `Tellus` (location)
        assert Tellus.objects.count() == 26

        # import the latest file `telling_data`
        # write fixture data
        filepath = os.path.dirname(os.path.abspath(__file__))
        with open('/tmp/tellus/tellus.csv', 'w') as f:
            f.write(open(
                "{}/fixture_files/AMS365_2016-10.csv".format(filepath)).read())

        self.my_importer.process_telling_data()
        assert TellusData.objects.count() == 34

        with open('/tmp/tellus/tellus.csv', 'w') as f:
            f.write(open(
                "{}/fixture_files/AMS365_2016-11.csv".format(filepath)).read())

        self.my_importer.process_telling_data()
        assert TellusData.objects.count() == 34
