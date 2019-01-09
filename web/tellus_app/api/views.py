"""
Tellus views
"""

from api import serializers

from django.contrib.gis.geos import Point  # noqa
from django.contrib.gis.measure import Distance

from datapunt_api.rest import DatapuntViewSet
from django_filters.rest_framework import DjangoFilterBackend

from api.countless_pagination import HALCursorCountlessPagination
from datasets.tellus_data import models
from datasets.tellus_data.models import Tellus


class MeetlocatieViewSet(DatapuntViewSet):
    """
    Returns all `LengteInterval instances`, ordered by id
    """
    queryset = models.Meetlocatie.objects.all().order_by('pk')
    serializer_class = serializers.MeetlocatieSerializer
    serializer_detail_class = serializers.MeetlocatieSerializer


class LengteIntervalViewSet(DatapuntViewSet):
    """
    Returns all `LengteInterval instances`, ordered by id
    """
    queryset = models.LengteInterval.objects.all().order_by('pk')
    serializer_class = serializers.LengteIntervalSerializer
    serializer_detail_class = serializers.LengteIntervalSerializer


class SnelheidsIntervalViewSet(DatapuntViewSet):
    """
    Returns all `SnelheidsInterval instances`, ordered by id
    """
    queryset = models.SnelheidsInterval.objects.all().order_by('pk')
    serializer_class = serializers.SnelheidsIntervalSerializer
    serializer_detail_class = serializers.SnelheidsIntervalSerializer


class SnelheidsCategorieViewSet(DatapuntViewSet):
    """
    Returns all `SnelheidsCategorie instances`, ordered by id
    """
    queryset = models.SnelheidsCategorie.objects.all().order_by('pk')
    serializer_class = serializers.SnelheidsCategorieSerializer
    serializer_detail_class = serializers.SnelheidsCategorieSerializer


class RepresentatiefCategorieViewSet(DatapuntViewSet):
    """
    Returns all `RepresentatiefCategorie instances`, ordered by id
    """
    queryset = models.RepresentatiefCategorie.objects.all().order_by('pk')
    serializer_class = serializers.RepresentatiefCategorieSerializer
    serializer_detail_class = serializers.RepresentatiefCategorieSerializer


class ValidatieCategorieViewSet(DatapuntViewSet):
    """
    Returns all `ValidatieCategorie instances`, ordered by id
    """
    queryset = models.ValidatieCategorie.objects.all().order_by('pk')
    serializer_class = serializers.ValidatieCategorieSerializer
    serializer_detail_class = serializers.ValidatieCategorieSerializer


class MeetraaiCategorieViewSet(DatapuntViewSet):
    """
    Returns all `MeetraaiCategorie instances`, ordered by id
    """
    queryset = models.MeetraaiCategorie.objects.all().order_by('pk')
    serializer_class = serializers.MeetraaiCategorieSerializer
    serializer_detail_class = serializers.MeetraaiCategorieSerializer


class TellusViewSet(DatapuntViewSet):
    queryset = models.Tellus.objects.all().order_by('pk')
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
                geometrie__distance_lte=(pnt, Distance(m=int(radius))))

        return Tellus.objects.all().order_by('pk')


class TellingViewSet(DatapuntViewSet):
    """
    Returns a list of `Telling` objects.
    """
    queryset = models.Telling.objects.all().order_by('pk')
    serializer_class = serializers.TellingSerializer
    serializer_detail_class = serializers.TellingSerializer


class TelRichtingViewSet(DatapuntViewSet):
    """
    Returns a list of `TelRichting instances`, ordered by id
    """
    queryset = models.TelRichting.objects.all().order_by('pk')
    serializer_class = serializers.TelRichtingSerializer
    serializer_detail_class = serializers.TelRichtingSerializer


class TellusDataCarsPerHourPerDayViewSet(DatapuntViewSet):
    """
    Returns a list of `TellusDataCarsPerHourPerDay` objects for:

    * Every Tellus
    * Every day
    * Every hour
    * Type of day
    * Sum of all cars passing within that hour slot
    """
    queryset = models.TellingCarsPerHourPerDay.objects.all().order_by('pk')
    serializer_class = serializers.TellingCarsPerHourPerDaySerializer
    serializer_detail_class = serializers.TellingCarsPerHourPerDaySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('dag_type', )
    # pagination_class = HALCursorCountlessPagination


class TellusDataCarsPerHourLengthViewSet(DatapuntViewSet):
    """
    Returns a list of `TellusDataCarsPerHourPerDay` objects for:

    * Every Tellus
    * Every day
    * Every hour
    * Every length
    * Type of day
    * Sum of all cars passing within that hour slot
    """
    queryset = models.TellingCarsPerHourLength.objects.all().order_by('pk')
    serializer_class = serializers.TellingCarsPerHourLengthSerializer
    serializer_detail_class = serializers.TellingCarsPerHourLengthSerializer
    pagination_class = HALCursorCountlessPagination


class TellusDataCarsPerHourSpeedViewSet(DatapuntViewSet):
    """
    Returns a list of `TellusDataCarsPerHourPerDay` objects for:

    * Every Tellus
    * Every day
    * Every hour
    * Every length
    * Type of day
    * Sum of all cars passing within that hour slot
    """
    queryset = models.TellingCarsPerHourSpeed.objects.all().order_by('pk')
    serializer_class = serializers.TellingCarsPerHourSpeedSerializer
    serializer_detail_class = serializers.TellingCarsPerHourSpeedSerializer
    pagination_class = HALCursorCountlessPagination
