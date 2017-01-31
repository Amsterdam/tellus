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
    lookup_field = 'klasse'


class SnelheidsCategorieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a SnelheidsCategorie instance
    list:
        Return all SnelheidsCategorie instances, ordered by id
    """
    queryset = SnelheidsCategorie.objects.all()
    serializer_class = SnelheidsCategorieSerializer
    lookup_field = 'klasse'


class TellusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a Tellus object instance
    list:
        Return all Tellus objects, ordered by objnr_vor
    """
    queryset = Tellus.objects.all()
    serializer_class = TellusSerializer
    lookup_field = 'id'


class TellusDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a Tellus data instance
    list:
        Return all Tellus data instances, ordered by date and time descending
    """
    queryset = TellusData.objects.all()
    serializer_class = TellusDataSerializer


# from rest_framework import mixins
# from rest_framework import generics
#
#
# class TellusDataList(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Tellus.objects.all()
#     serializer_class = TellusDataSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class TellusDataDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = TellusData.objects.all()
#     serializer_class = TellusDataSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
