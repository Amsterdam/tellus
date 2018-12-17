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

        def import_meta(self, codebook_filename):
            print('HERE', codebook_filename)
            filepath = os.path.dirname(os.path.abspath(__file__))
            wb = openpyxl.load_workbook(
                "{}/fixture_files/{}".format(filepath, codebook_filename))
            return {
                sheet_name: wb.get_sheet_by_name(sheet_name)
                for sheet_name in wb.get_sheet_names()}

        # patch `_import_meta`
        TellusImporter._import_meta = import_meta
        self.my_importer = TellusImporter(
            codebook="metadata.xlsx",
            codebook_addon="metadata_aanvulling.xlsx")

    def test_import_meta(self):
        # check if _import_meta has loaded XLS file
        assert len(self.my_importer.codebook_addon_sheets) == 1
        assert len(self.my_importer.codebook_sheets) == 7

    def test_process_tellus_import(self):
        self.my_importer.process_lengte_interval()
        self.my_importer.process_snelheids_categorie()
        assert SnelheidsCategorie.objects.count() == 4
        # import the `tellus_locaties`
        self.my_importer.process_tellus_locaties()

        # count the number of rows imported in `Tellus` (location)
        assert Tellus.objects.count() == 26

        # import the latest file `telling_data`
        # write fixture data
        os.makedirs('/tmp/tellus', exist_ok=True)
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
        assert TellusData.objects.count() == 68
