"""
Tellus views
"""

from datasets.tellus_data.models import Tellus, TellusData
from datasets.tellus_data.models import LengteCategorie, SnelheidsCategorie

from api import serializers

from datapunt_api import rest


class LengteCategorieViewSet(rest.DatapuntViewSet):
    """
    Returns all `LengteCategorie instances`, ordered by id
    """
    queryset = LengteCategorie.objects.all().order_by('pk')
    serializer_class = serializers.LengteCategorieSerializer
    serializer_detail_class = serializers.LengteCategorieSerializer


class SnelheidsCategorieViewSet(rest.DatapuntViewSet):
    """
    Returns all `SnelheidsCategorie instances`, ordered by id
    """
    queryset = SnelheidsCategorie.objects.all().order_by('pk')
    serializer_class = serializers.SnelheidsCategorieSerializer
    serializer_detail_class = serializers.SnelheidsCategorieSerializer


class TellusViewSet(rest.DatapuntViewSet):
    queryset = Tellus.objects.all().order_by('pk')
    serializer_class = serializers.TellusSerializer
    serializer_detail_class = serializers.TellusSerializer

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
                geometrie__distance_lte=(pnt, D(m=int(radius))))

        return Tellus.objects.all()


class TellusDataViewSet(rest.DatapuntViewSet):
    """
    Returns a list of `TellusData` objects.
    """
    queryset = TellusData.objects.all()
    serializer_class = serializers.TellusDataSerializer
    serializer_detail_class = serializers.TellusDataSerializer
