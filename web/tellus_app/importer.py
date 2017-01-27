import csv
import logging
import os

import django
import openpyxl
from dateutil.parser import parse as parse_date

django.setup()

from django.contrib.gis.geos import Point


from datasets.tellus_data.models import (Tellus, SnelheidsKlasse, TellusData)
from objectstore.objectstore import fetch_meta_data, fetch_last_tellus_data

log = logging.getLogger(__name__)

OBJSTORE_METADATA = 'meta'


class TellusImporter(object):
    def __init__(self, codebook_name="AMS365_codeboek_v5.xlsx"):
        self.codebook_name = codebook_name
        self.sheets = {}
        self._import_meta()

    def _import_meta(self):
        """
        Function that retrieves the meta data from a Objectstore
        """
        os.makedirs("/tmp/tellus", exist_ok=True)
        with open("/tmp/tellus/{}".format(self.codebook_name), 'wb') as f:
            f.write(fetch_meta_data(self.codebook_name))

        wb = openpyxl.load_workbook("/tmp/tellus/{}".format(self.codebook_name))
        self.sheets = {sheet_name: wb.get_sheet_by_name(sheet_name) for sheet_name in wb.get_sheet_names()}

    def decodedata(self, filebytes):
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

    def process_tellus_locaties(self, sheet_name='Locaties', title_row=1, first_col=0):
        """
        Import the data for the Tellus (Locations)
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        for row in self.sheets[sheet_name].iter_rows(min_row=title_row + 1, min_col=first_col):
            res = [cell.value for cell in row]

            if res[0]:  # probaly an empty row
                db_row, created = Tellus.objects.update_or_create(
                    id=int(res[1][5:]),  # format = 'AMSTDxxx'
                    objnr_vor=res[0], objnr_leverancier=res[1], standplaats=res[2],
                    zijstraat_a=res[3], zijstraat_b=res[4],
                    richting_1=res[5], richting_2=res[6],
                    rijksdriehoek_x=res[7], rijksdriehoek_y=res[8],
                    latitude=res[9], longitude=res[10], snelheids_klasse_id=res[11],
                    geometrie=Point(float(res[7]), float(res[8]), srid=28992))
                if created:
                    log.info("Created {}".format(str(db_row)))
                else:
                    log.info("Updated {}".format(str(db_row)))

    def process_snelheids_klasse(self, sheet_name='Snelheidscategorieen', title_row=1, first_col=1):
        """
        Import SnelheidsKlasse objects
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        for row in self.sheets[sheet_name].iter_rows(min_row=title_row + 1, max_row=5, min_col=first_col):
            res = [cell.value for cell in row]

            db_row, created = SnelheidsKlasse.objects.update_or_create(
                klasse=int(res[0]),
                s1=res[1], s2=res[2], s3=res[3], s4=res[4], s5=res[5],
                s6=res[6], s7=res[7], s8=res[8], s9=res[9], s10=res[10])
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def temp_tellus_data(self):
        with open('/tmp/tellus/tellus.csv', 'wb') as f:
            f.write(fetch_last_tellus_data())

    def process_telling_data(self):

        with open('/tmp/tellus/tellus.csv') as csvfile:
            my_reader = csv.reader(csvfile, dialect='excel', delimiter=';')
            next(my_reader, None)
            for trow in my_reader:
                try:
                    tellus_object = Tellus.objects.get(id=trow[0])
                    r_start = tellus_object.snelheids_klasse.klasse + 8  # add index of field C1
                    db_row, created = TellusData.objects.update_or_create(
                        tellus=tellus_object,
                        tijd_van=parse_date(trow[6]),
                        tijd_tot=parse_date(trow[7]),
                        defaults={
                            'tellus': tellus_object,
                            'tijd_van': parse_date(trow[6]),
                            'tijd_tot': parse_date(trow[7]),
                            'lengte_categorie': trow[5],
                            'richting': trow[1],
                            'validatie': trow[2],
                            'representatief': trow[3],
                            'meetraai': trow[4],
                            'meting_1': trow[r_start],
                            'meting_2': trow[r_start + 1],
                            'meting_3': trow[r_start + 2],
                            'meting_4': trow[r_start + 3],
                            'meting_5': trow[r_start + 4],
                            'meting_6': trow[r_start + 5],
                            'meting_7': trow[r_start + 6],
                            'meting_8': trow[r_start + 7],
                            'meting_9': trow[r_start + 8],
                            'meting_10': trow[r_start + 9]}
                        )
                    if created:
                        log.debug("Created {}".format(str(db_row)))
                    else:
                        log.debug("Updated {}".format(str(db_row)))
                except Tellus.DoesNotExist:
                    # Log not found message and continue
                    log.error("Tellus {}-{} does not exist".format(trow[0], trow[1]))


if __name__ == "__main__":
    os.makedirs('/tmp/tellus', exist_ok=True)
    importer = TellusImporter()
    importer.process_snelheids_klasse()
    importer.process_tellus_locaties()
    # importer.temp_tellus_data()
    # importer.process_telling_data()
    log.info("Done importing tellus data")
