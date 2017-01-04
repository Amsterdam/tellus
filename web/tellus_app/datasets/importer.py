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
            res = []
            for cell in row:
                    res.append(cell.value)

    meetlocatie
    richtingcode
    telpunt
    straat
    windrichting = models.CharField(max_length=20, blank=True, null=True)
    zijstraat = models.CharField(max_length=256, blank=True, null=True)
    richting = models.CharField(max_length=256)

            db_row = Locatie.objects.insert_or_update(
                meetlocatie=res[0], richtingcode=res[1], telpunt=res[2], straat=res[3], windrichting=res[4], zijstraat=res[5])
            print(res)
