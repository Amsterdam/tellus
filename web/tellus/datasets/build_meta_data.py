import logging
import openpyxl

from objectstore.objectstore import get_flobj_from_objectstore
from .tellus_data.tellus_mixins import generic_mixin

log = logging.getLogger(__name__)

OBJSTORE_METADATA = 'meta'


class TellusMeta(generic_mixin):

    def process_sheet(self, sheet):
        print(sheet)

    def get_data(self):
        return get_flobj_from_objectstore(OBJSTORE_METADATA + '/' + 'metadata.xlsx')

    def ImportMeta(self):
        """
        Function that retrieves the meta data from the objectstore,
        reads it and stores it in the database

        Read from the objectstore from separate subdirectory meta (METADATA)
        """

        flobjs = self.get_data()

        for flo in flobjs:
            wb = openpyxl.load_workbook(flo)
            for sheet_name in wb.sheetnames:
                sheet = wb.get_sheet_by_name(sheet_name)
                self.process_sheet(sheet)

        return
