"""
Tellus views
"""

from api import serializers

from django.contrib.gis.geos import Point  # noqa
from django.contrib.gis.measure import Distance

from datapunt_api.rest import DatapuntViewSet

from datasets.tellus_data.models import LengteCategorie
from datasets.tellus_data.models import SnelheidsCategorie
from datasets.tellus_data.models import Tellus
from datasets.tellus_data.models import TellusData

from api.serializers import LengteCategorieSerializer
from api.serializers import SnelheidsCategorieSerializer
from api.serializers import TellusSerializer
from api.serializers import TellusDataSerializer


class LengteCategorieViewSet(DatapuntViewSet):
    """
    Returns all `LengteCategorie instances`, ordered by id
    """
    queryset = LengteCategorie.objects.all().order_by('pk')
    serializer_class = LengteCategorieSerializer
    serializer_detail_class = LengteCategorieSerializer


class SnelheidsCategorieViewSet(DatapuntViewSet):
    """
    Returns all `SnelheidsCategorie instances`, ordered by id
    """
    queryset = SnelheidsCategorie.objects.all().order_by('pk')
    serializer_class = SnelheidsCategorieSerializer
    serializer_detail_class = SnelheidsCategorieSerializer

class TellusViewSet(DatapuntViewSet):
    queryset = Tellus.objects.all().order_by('pk')
    serializer_class = TellusSerializer
    serializer_detail_class = TellusSerializer

    def get_queryset(self):
        """
        Filtering using latitude, longitude and radius
        """
        lat = self.request.query_params.get('lat', None)
        lon = self.request.query_params.get('lon', None)
        radius = self.request.query_params.get('radius', None)
        if lat is not None and lon is not None and radius is not None:
            pnt = Point(float(lon), float(lat), srid=4326)
            return Tellus.objects.filter(
                geometrie__distance_lte=(pnt, Distance(m=int(radius))))

        return Tellus.objects.all()


class TellusDataViewSet(DatapuntViewSet):
    """
    Returns a list of `TellusData` objects.
    """
    queryset = TellusData.objects.all()
    serializer_class = TellusDataSerializer
    serializer_detail_class = TellusDataSerializer
