import csv
import logging
import os

import django
import openpyxl
import pytz
from dateutil.parser import parse as parse_date

django.setup()

from django.contrib.gis.geos import Point  # noqa
from datasets.tellus_data.models import (Tellus, SnelheidsCategorie,
                                         LengteCategorie, TellusData)  # noqa
from objectstore.objectstore import fetch_meta_data, fetch_tellus_data_file_object, fetch_tellus_data_file_names  # noqa

log = logging.getLogger(__name__)

OBJSTORE_METADATA = 'meta'

functional_errors = []


class TellusImporter(object):

    tellus_number_cache = []

    def __init__(self, codebook, codebook_addon):
        self.codebook_sheets = self._import_meta(codebook)
        self.codebook_addon_sheets = self._import_meta(codebook_addon)

    def _import_meta(self, codebook_filename):
        """
        Function that retrieves the meta data from a Objectstore
        """
        os.makedirs("/tmp/tellus", exist_ok=True)
        with open("/tmp/tellus/{}".format(codebook_filename), 'wb') as f:
            f.write(fetch_meta_data(codebook_filename))

        wb = openpyxl.load_workbook("/tmp/tellus/{}".format(codebook_filename))
        return {sheet_name: wb.get_sheet_by_name(sheet_name) for
                sheet_name in wb.get_sheet_names()}

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

    def process_tellus_locaties(self, sheet_name='Locaties', title_row=1,
                                first_col=0):
        """
        Import the data for the Tellus (Locations)
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        for row in self.codebook_addon_sheets[sheet_name].iter_rows(
                min_row=title_row + 1,
                min_col=first_col):
            res = [cell.value for cell in row]

            if res[0]:  # probaly an empty row
                db_row, created = Tellus.objects.update_or_create(
                    id=int(res[1][5:]),  # format = 'AMSTDxxx'
                    objnr_vor=res[0], objnr_leverancier=res[1],
                    standplaats=res[2],
                    zijstraat_a=res[3], zijstraat_b=res[4],
                    richting_1=res[5], richting_2=res[6],
                    rijksdriehoek_x=res[7], rijksdriehoek_y=res[8],
                    latitude=res[9], longitude=res[10],
                    snelheids_klasse_id=res[11],
                    geometrie=Point(float(res[7]), float(res[8]), srid=28992))
                if created:
                    log.info("Created {}".format(str(db_row)))
                else:
                    log.info("Updated {}".format(str(db_row)))

    def process_snelheids_categorie(self, sheet_name='Snelheidscategorieen',
                                    title_row=1, first_col=1):
        """
        Import SnelheidsCategorie objects
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        for row in self.codebook_sheets[sheet_name].iter_rows(min_row=title_row + 1,
                                                              max_row=5,
                                                              min_col=first_col):
            res = [cell.value for cell in row]

            db_row, created = SnelheidsCategorie.objects.update_or_create(
                klasse=int(res[0]),
                s1=res[1], s2=res[2], s3=res[3], s4=res[4], s5=res[5],
                s6=res[6], s7=res[7], s8=res[8], s9=res[9], s10=res[10])
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def process_lengte_categorie(self, sheet_name='Lengtecategorieen',
                                 title_row=1, first_col=1):
        """
        Import LengteCategorie objects
        :param sheet_name:
        :param title_row:
        :param first_col:
        :return:
        """
        for row in self.codebook_sheets[sheet_name].iter_rows(min_row=title_row + 1,
                                                              max_row=2,
                                                              min_col=first_col):
            res = [cell.value for cell in row]

            db_row, created = LengteCategorie.objects.update_or_create(
                klasse=int(res[0]),
                l1=res[1], l2=res[2], l3=res[3], l4=res[4], l5=res[5],
                l6=res[6])
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def temp_tellus_data(self, file_name):
        with open('/tmp/tellus/tellus.csv', 'wb') as f:
            f.write(fetch_tellus_data_file_object(file_name))

    def determine_tellus_number(self, location, direction):
        # lokaties, waarbij iedere richting een eigen tellus object heeft
        dual_locations = (12, 17, 22, 29)
        if direction == '2' and dual_locations.__contains__(int(location)):
            nr = int(location) + 1
        else:
            nr = int(location)
        return nr

    def get_tellus(self, location, direction):
        tellus_number = self.determine_tellus_number(location, direction)
        if tellus_number in self.tellus_number_cache:
            return tellus_number
        try:
            tellus = Tellus.objects.get(id=tellus_number)
            self.tellus_number_cache += [tellus.id]
            return tellus.id
        except Tellus.DoesNotExist:
            # Log not found message and continue
            message = "Geen metadata gevonden voor: meetraai {}, richting {}, tellus nummer {}.".format(
                location, direction, tellus_number
            )
            if message not in functional_errors:
                functional_errors.append(message)
            log.error(message)
            Tellus.objects.update_or_create(id=tellus_number,
                                            objnr_leverancier='AMSTD' + str(tellus_number).zfill(3))
            self.tellus_number_cache += [tellus_number]
            return tellus_number

    def process_telling_data(self):

        with open('/tmp/tellus/tellus.csv') as csvfile:
            my_reader = csv.reader(csvfile, dialect='excel', delimiter=';')
            next(my_reader, None)
            for trow in my_reader:
                try:
                    tellus_id = self.get_tellus(trow[0], trow[1])

                    snelheids_categorie_object = SnelheidsCategorie.objects.get(klasse=int(trow[5]))
                    lengte_categorie_object = LengteCategorie.objects.get(klasse=1)
                    tijd_van = parse_date(trow[6]).replace(tzinfo=pytz.UTC)
                    tijd_tot = parse_date(trow[7]).replace(tzinfo=pytz.UTC)

                    db_row, created = TellusData.objects.update_or_create(
                        tellus_id=tellus_id,
                        richting=trow[1],
                        tijd_van=tijd_van,
                        tijd_tot=tijd_tot,
                        c1=trow[8], c2=trow[9], c3=trow[10], c4=trow[11], c5=trow[12], c6=trow[13],
                        c7=trow[14], c8=trow[15], c9=trow[16], c10=trow[17], c11=trow[18], c12=trow[19],
                        c13=trow[20], c14=trow[21], c15=trow[22], c16=trow[23], c17=trow[24], c18=trow[25],
                        c19=trow[26], c20=trow[27], c21=trow[28], c22=trow[29], c23=trow[30], c24=trow[31],
                        c25=trow[32], c26=trow[33], c27=trow[34], c28=trow[35], c29=trow[36], c30=trow[37],
                        c31=trow[38], c32=trow[39], c33=trow[40], c34=trow[41], c35=trow[42], c36=trow[43],
                        c37=trow[44], c38=trow[45], c39=trow[46], c40=trow[47], c41=trow[48], c42=trow[49],
                        c43=trow[50], c44=trow[51], c45=trow[52], c46=trow[53], c47=trow[54], c48=trow[55],
                        c49=trow[56], c50=trow[57], c51=trow[58], c52=trow[59], c53=trow[60], c54=trow[61],
                        c55=trow[62], c56=trow[63], c57=trow[64], c58=trow[65], c59=trow[66], c60=trow[67],
                        defaults={
                            'tellus_id': tellus_id,
                            'snelheids_categorie': snelheids_categorie_object,
                            'tijd_van': tijd_van,
                            'tijd_tot': tijd_tot,
                            'lengte_categorie': lengte_categorie_object,
                            'richting': trow[1],
                            'validatie': trow[2],
                            'representatief': trow[3],
                            'meetraai': trow[4],
                        }
                    )
                    if created:
                        log.debug("Created {}".format(str(db_row)))
                    else:
                        log.debug("Updated {}".format(str(db_row)))
                except Tellus.DoesNotExist:
                    # Log not found message and continue
                    log.error(
                        "Tellus {}-{} does not exist".format(trow[0], trow[1]))


if __name__ == "__main__":
    assert os.getenv('TELLUS_OBJECTSTORE_PASSWORD')

    os.makedirs('/tmp/tellus', exist_ok=True)
    importer = TellusImporter(codebook='AMS365_codeboek_v5.xlsx',
                              codebook_addon='AMS365_codeboek_v5_aanvulling.xlsx')
    importer.process_lengte_categorie()
    importer.process_snelheids_categorie()
    importer.process_tellus_locaties()
    for file_name in fetch_tellus_data_file_names():
        importer.temp_tellus_data(file_name)
        importer.process_telling_data()
    for e in functional_errors:
        log.info(e)

    log.info("Done importing tellus data")
