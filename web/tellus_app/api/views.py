from datasets.tellus_data.models import LengteCategorie, SnelheidsCategorie, Tellus, TellusData
from rest_framework import mixins, generics
from api import serializers


class LengteCategorieList(mixins.ListModelMixin, generics.GenericAPIView):
    """
    Returns all `LengteCategorie instances`, ordered by id
    """
    queryset = LengteCategorie.objects.all().order_by('pk')
    serializer_class = serializers.LengteCategorieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class LengteCategorieDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    Returns `LengteCategorie` instance by id
    """
    queryset = Tellus.objects.all()
    serializer_class = serializers.LengteCategorieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SnelheidsCategorieList(mixins.ListModelMixin, generics.GenericAPIView):
    """
    Returns all `SnelheidsCategorie instances`, ordered by id
    """
    queryset = SnelheidsCategorie.objects.all().order_by('pk')
    serializer_class = serializers.SnelheidsCategorieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SnelheidsCategorieDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = SnelheidsCategorie.objects.all()
    serializer_class = serializers.SnelheidsCategorieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TellusList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Tellus.objects.all().order_by('pk')
    serializer_class = serializers.TellusSerializer

    # pagination_class = HALPagination
    # filter_backends = (filters.DjangoFilterBackend,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TellusDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    Returns a `Tellus detail` object by id
    """
    queryset = Tellus.objects.all()
    serializer_class = serializers.TellusSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TellusDataList(mixins.ListModelMixin, generics.GenericAPIView):
    """
    Returns a list of `TellusData` objects.
    """
    queryset = TellusData.objects.all()
    serializer_class = serializers.TellusDataSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TellusDataDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    Returns a `TellusData detail` object by id
    """
    queryset = TellusData.objects.all()
    serializer_class = serializers.TellusDataSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
