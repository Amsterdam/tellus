import os

import pytz
from dateutil.parser import parse as parse_date
from unittest import mock

import openpyxl
from django.test import TestCase

from datasets.tellus_data.models import (
    Tellus,
    SnelheidsCategorie,
    Telling,
    SnelheidsInterval,
    Meetlocatie,
    TelRichting,
    LengteInterval,
)
from importer_lib.importer import TellusImporter, import_telling

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURE_DIR = path = os.path.join(TEST_DIR, "fixture_files/")


class TestImport(TestCase):
    @mock.patch("importer_lib.importer.TellusImporter._import_meta")
    def setUp(self, patched_import_meta):
        os.putenv("TELLUS_OBJECTSTORE_PASSWORD", "insecure")
        assert patched_import_meta == TellusImporter._import_meta

        def import_meta(self, codebook_filename):
            wb = openpyxl.load_workbook(os.path.join(FIXTURE_DIR, codebook_filename))
            return {sheet_name: wb[sheet_name] for sheet_name in wb.sheetnames}

        # patch `_import_meta`
        TellusImporter._import_meta = import_meta
        self.my_importer = TellusImporter(
            codebook="metadata.xlsx", codebook_addon="metadata_aanvulling.xlsx"
        )

    def test_import_meta(self):
        # check if _import_meta has loaded XLS file
        assert len(self.my_importer.codebook_addon_sheets) == 1
        assert len(self.my_importer.codebook_sheets) == 7

    def test_process_tellus_import(self):
        self.my_importer.process_meetraai_categorie()
        self.my_importer.process_representatief_categorie()
        self.my_importer.process_validatie_categorie()

        self.my_importer.process_lengte_interval()
        lengteInterval = LengteInterval.objects.get(id=1)
        self.assertEqual(lengteInterval.label, "0 - 5,1 m")

        self.my_importer.process_snelheids_categorie()
        self.assertEqual(SnelheidsInterval.objects.count(), 20)
        snelheidsInterval = SnelheidsCategorie.objects.get(
            categorie=1, index=1
        ).interval
        self.assertEqual(snelheidsInterval.label, "< 30 km/u")

        self.my_importer.process_tellus_locaties()
        self.assertEqual(Tellus.objects.count(), 30)
        self.assertEqual(Meetlocatie.objects.count(), 26)
        telRichting = TelRichting.objects.get(tellus__meetlocatie=29, richting=2)
        self.assertEqual(telRichting.naam, "Prins Hendrikkade")
        self.assertEqual(telRichting.zijstraat, "Nieuwezijds Armsteeg")

        import_telling(os.path.join(FIXTURE_DIR, "AMS365_2016-10.csv"))
        self.assertEqual(Telling.objects.count(), 2040)

        import_telling(os.path.join(FIXTURE_DIR, "AMS365_2016-11.csv"))
        self.assertEqual(Telling.objects.count(), 4080)
        time = parse_date("2016-11-11T22:00:00").replace(tzinfo=pytz.UTC)
        telling = Telling.objects.get(
            tijd_van=time,
            tel_richting=telRichting.pk,
            snelheids_interval=snelheidsInterval.pk,
            lengte_interval=lengteInterval.pk,
        )
        self.assertEqual(
            telling.aantal, 37
        )  # Value c1 for last row of 'AMS365_2016-11.csv'
