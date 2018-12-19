
from datapunt_api.pagination import HALCursorPagination


class HALCursorCountlessPagination(HALCursorPagination):
    page_size=1000
    ordering='id'
    count_table=False
