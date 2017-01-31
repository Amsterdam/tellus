from rest_framework import viewsets

from datasets.tellus_data.models import LengteCategorie, SnelheidsCategorie, Tellus, TellusData
from .serializers import (
    LengteCategorieSerializer, SnelheidsCategorieSerializer, TellusSerializer, TellusDataSerializer)


class LengteCategorieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a `LengteCategorie` instance
    list:
        Return all `LengteCategorie instances`, ordered by id
    """
    queryset = LengteCategorie.objects.all()
    serializer_class = LengteCategorieSerializer
    # lookup_field = 'klasse'


class SnelheidsCategorieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a SnelheidsCategorie instance
    list:
        Return all SnelheidsCategorie instances, ordered by id
    """
    queryset = SnelheidsCategorie.objects.all()
    serializer_class = SnelheidsCategorieSerializer
    # lookup_field = 'klasse'


class TellusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a Tellus object instance
    list:
        Return all Tellus objects, ordered by objnr_vor
    """
    queryset = Tellus.objects.all()
    serializer_class = TellusSerializer
    # lookup_field = 'objnr_vor'


class TellusDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a Tellus data instance
    list:
        Return all Tellus data instances, ordered by date and time descending
    """
    queryset = TellusData.objects.all()
    serializer_class = TellusDataSerializer
