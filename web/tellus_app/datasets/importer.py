import logging
import openpyxl

# from objectstore.objectstore import get_flobj_from_objectstore
# from datasets.tellus_data.tellus_mixins import generic_mixin

from datasets.tellus_data.models import Locatie
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
                meetlocatie=res[0], richtingcode=res[1], telpunt=res[2],
                straat=res[3], windrichting=res[4], zijstraat1=res[5])
            if created:
                log.info("Created location {}".format(str(db_row)))
            else:
                log.info("Updated location {}".format(str(db_row)))
