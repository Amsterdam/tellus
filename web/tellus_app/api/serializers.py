import json

from rest_framework import serializers

from datasets.tellus_data.models import LengteCategorie, SnelheidsCategorie, Tellus, TellusData
from .rest import DataSetSerializerMixin, HALSerializer


class TellusMixin(DataSetSerializerMixin):
    dataset = 'tellus_data'


class TellusSerializer(TellusMixin, HALSerializer):
    class Meta:
        model = Tellus
        fields = '__all__'


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
    meet_resultaten = serializers.SerializerMethodField()

    class Meta:
        model = TellusData
        fields = (
            'tellus',
            'snelheids_categorie',
            'lengte_categorie',
            'tijd_van',
            'tijd_tot',
            'richting',
            'validatie',
            'representatief',
            'meetraai',
            'meet_resultaten',
        )
        extra_kwargs = {
            'tellus': {'view_name': 'tellus-detail', 'lookup_field': 'pk'},
            'snelheids_categorie': {'view_name': 'snelheidscategorie-detail', 'lookup_field': 'pk'},
            'lengte_categorie': {'view_name': 'lengtecategorie-detail', 'lookup_field': 'pk'}
        }

    def get_meet_resultaten(self, obj):
        return json.loads(obj.data)

        # def get_radius(self, obj):
        #     return "BLA"
