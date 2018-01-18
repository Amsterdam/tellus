import authorization_levels
from datasets.tellus_data.models import LengteCategorie, SnelheidsCategorie, Tellus, TellusData
from rest_framework import serializers

from .rest import DataSetSerializerMixin, HALSerializer


class TellusMixin(DataSetSerializerMixin):
    dataset = 'tellus_data'


class TellusSerializer(TellusMixin, HALSerializer):
    _display = serializers.SerializerMethodField()

    class Meta:
        model = Tellus
        fields = (
            '_display',
            'id',
            'objnr_vor',
            'objnr_leverancier',
            'snelheids_klasse',
            'standplaats',
            'zijstraat_a',
            'zijstraat_b',
            'richting_1',
            'richting_2',
            'latitude',
            'longitude',
            'rijksdriehoek_x',
            'rijksdriehoek_y',
            'geometrie',
        )

    def get__display(self, obj):
        return str(obj)


class LengteCategorieSerializer(TellusMixin, HALSerializer):
    class Meta:
        model = LengteCategorie
        fields = (
            'klasse',
            'l1',
            'l2',
            'l3',
            'l4',
            'l5',
            'l6',
        )


class SnelheidsCategorieSerializer(TellusMixin, HALSerializer):
    class Meta:
        model = SnelheidsCategorie
        fields = (
            'klasse',
            's1',
            's2',
            's3',
            's4',
            's5',
            's6',
            's7',
            's8',
            's9',
            's10',
        )


class TellusDataSerializer(TellusMixin, HALSerializer):
    _display = serializers.SerializerMethodField()

    class Meta:
        model = TellusData
        fields = (
            '_display',
            'tellus',
            'snelheids_categorie',
            'lengte_categorie',
            'tijd_van',
            'tijd_tot',
            'richting',
            'validatie',
            'representatief',
            'meetraai',
            'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
            'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19',
            'c20', 'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29',
            'c30', 'c31', 'c32', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c39',
            'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49',
            'c50', 'c51', 'c52', 'c53', 'c54', 'c55', 'c56', 'c57', 'c58', 'c59',
            'c60',
        )
        extra_kwargs = {
            'tellus': {'view_name': 'tellus-detail', 'lookup_field': 'pk'},
            'snelheids_categorie': {'view_name': 'snelheidscategorie-detail', 'lookup_field': 'pk'},
            'lengte_categorie': {'view_name': 'lengtecategorie-detail', 'lookup_field': 'pk'}
        }

    def get__display(self, obj):
        return str(obj)
