import csv
import logging
import openpyxl
import django
django.setup()

from datasets.tellus_data.models import (Locatie, LengteCategorie, SnelheidsCategorie, Telling)

log = logging.getLogger(__name__)

OBJSTORE_METADATA = 'meta'


class MetaImporter(object):
    def __init__(self):
        self.sheets = {}
        self._import_meta()

    def _import_meta(self):
        """
        Function that retrieves the meta data from a file (use Objectstore later on)
        """
        wb = openpyxl.load_workbook('/tmp/tellus/AMS365_Codeboek.xlsx')
        self.sheets = {sheet_name: wb.get_sheet_by_name(sheet_name) for sheet_name in wb.get_sheet_names()}

    def process_locaties(self, sheet_name='Locaties', title_row=2, first_col=2):
        for row in self.sheets[sheet_name].iter_rows(min_row=title_row + 1, min_col=first_col):
            res = [cell.value for cell in row]

            db_row, created = Locatie.objects.update_or_create(
                meetlocatie=res[0], richting=res[1], telpunt=res[2],
                straat=res[3], windrichting=res[4], zijstraat1=res[5])
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def process_lengte_categorie(self, sheet_name='Lengtecategorieen', title_row=1, first_col=2):
        ids = list(
            self.sheets[sheet_name].iter_rows(
                min_row=title_row, max_row=title_row, min_col=first_col))[0]
        values = list(
            self.sheets[sheet_name].iter_rows(
                min_row=title_row + 1, max_row=title_row + 1, min_col=first_col))[0]
        for r in range(5):
            val = values[r].value.split('-')
            print("`{}`".format(ids[r].value))
            db_row, created = LengteCategorie.objects.update_or_create(
                categorie=ids[r].value,
                lengte_van=val[0].replace(' ', ''),
                lengte_tot=val[1].replace(' ', '').replace('m', ' m'))
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def process_snelheids_categorie(self, sheet_name='Snelheidscategorieen', title_row=1, first_col=1):
        for row in self.sheets[sheet_name].iter_rows(min_row=title_row + 1, max_row=5, min_col=first_col):
            res = [cell.value for cell in row]

            db_row, created = SnelheidsCategorie.objects.update_or_create(
                categorie=res[0],
                s1=res[1], s2=res[2], s3=res[3], s4=res[4], s5=res[5],
                s6=res[6], s7=res[7], s8=res[8], s9=res[9], s10=res[10])
            if created:
                log.info("Created {}".format(str(db_row)))
            else:
                log.info("Updated {}".format(str(db_row)))

    def process_telling_data(self):
        with open('/tmp/tellus/AMS365_2016-10.csv') as csvfile:
            my_reader = csv.reader(csvfile, dialect='excel', delimiter=';')
            next(my_reader, None)
            for row in my_reader:
                db_row, created = Telling.objects.update_or_create(
                    meetlocatie=row[0], richting=row[1], validatie=row[2], representatief=row[3],
                    meetraai=row[4], classificatie=row[5], tijd_van=row[6], tijd_tot=row[7],
                    c1=row[8], c2=row[9], c3=row[10], c4=row[11], c5=row[12], c6=row[13], c7=row[14],
                    c8=row[15], c9=row[16], c10=row[17], c11=row[18], c12=row[19], c13=row[20], c14=row[21],
                    c15=row[22], c16=row[23], c17=row[24], c18=row[25], c19=row[26], c20=row[27], c31=row[28],
                    c32=row[29], c33=row[30], c34=row[31], c35=row[32], c36=row[33], c37=row[34], c38=row[35],
                    c39=row[36], c40=row[37], c41=row[38], c42=row[39], c43=row[40], c44=row[41], c45=row[42],
                    c46=row[43], c47=row[44], c48=row[45], c49=row[46], c50=row[47], c51=row[48], c52=row[49],
                    c53=row[20], c54=row[21], c55=row[22], c56=row[23], c57=row[24], c58=row[25], c59=row[26],
                    c60=row[27],
                )
                if created:
                    log.info("Created {}".format(str(db_row)))
                else:
                    log.info("Updated {}".format(str(db_row)))


if __name__ == "__main__":

    importer = MetaImporter()

    importer.process_snelheids_categorie()
    importer.process_lengte_categorie()
    importer.process_locaties()
    importer.process_telling_data()

    log.info("Done importing tellus data")
