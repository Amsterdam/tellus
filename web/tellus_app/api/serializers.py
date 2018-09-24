from rest_framework import serializers

from datapunt_api.rest import HALSerializer

from datasets.tellus_data.models import LengteCategorie
from datasets.tellus_data.models import SnelheidsCategorie
from datasets.tellus_data.models import Tellus
from datasets.tellus_data.models import TellusRichting
from datasets.tellus_data.models import TellusData
from datasets.tellus_data.models import TellusDataCarsPerHourPerDay


class TellusSerializer(HALSerializer):
    """
    Tellus details
    """

    dataset = 'tellus_data'
    _display = serializers.SerializerMethodField()

    class Meta(object):
        model = Tellus
        fields = (
            "_display",
            "id",
            "objnr_vor",
            "objnr_leverancier",
            "snelheids_klasse",
            "standplaats_id",
            "standplaats",
            "zijstraat_a",
            "zijstraat_b",
            "richting_1",
            "richting_2",
            "latitude",
            "longitude",
            "rijksdriehoek_x",
            "rijksdriehoek_y",
            "geometrie",
        )

    def get__display(self, obj):
        return str(obj)


class LengteCategorieSerializer(HALSerializer):
    """
    Lengte Categoriëen.
    """
    dataset = 'tellus_data'

    class Meta(object):
        model = LengteCategorie
        fields = (
            "klasse",
            "l1",
            "l2",
            "l3",
            "l4",
            "l5",
            "l6",
        )


class SnelheidsCategorieSerializer(HALSerializer):
    """Categorien.
    """
    dataset = 'tellus_data'

    class Meta(object):
        model = SnelheidsCategorie
        fields = (
            "klasse",
            "s1",
            "s2",
            "s3",
            "s4",
            "s5",
            "s6",
            "s7",
            "s8",
            "s9",
            "s10",
        )


class TellusDataSerializer(HALSerializer):
    """
    Tellus tellingen.
    """
    dataset = 'tellus_data'
    _display = serializers.SerializerMethodField()

    class Meta(object):
        model = TellusData
        fields = (
            "_display",
            "tellus",
            "snelheids_categorie",
            "lengte_categorie",
            "tijd_van",
            "tijd_tot",
            "richting",
            "validatie",
            "representatief",
            "meetraai",
            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9",
            "c10", "c11", "c12", "c13", "c14", "c15", "c16", "c17", "c18", "c19",
            "c20", "c21", "c22", "c23", "c24", "c25", "c26", "c27", "c28", "c29",
            "c30", "c31", "c32", "c33", "c34", "c35", "c36", "c37", "c38", "c39",
            "c40", "c41", "c42", "c43", "c44", "c45", "c46", "c47", "c48", "c49",
            "c50", "c51", "c52", "c53", "c54", "c55", "c56", "c57", "c58", "c59",
            "c60",
        )
        extra_kwargs = {
            "tellus": {"view_name": "tellus-detail", "lookup_field": "pk"},
            "snelheids_categorie": {"view_name": "snelheidscategorie-detail", "lookup_field": "pk"},
            "lengte_categorie": {"view_name": "lengtecategorie-detail", "lookup_field": "pk"}
        }

    def get__display(self, obj):
        return str(obj)


class TellusRichtingSerializer(HALSerializer):
    """
    Tellus Werkdag, Weekdag totalen
    """
    dataset = 'tellus_data'
    _display = serializers.SerializerMethodField()

    class Meta(object):
        model = TellusRichting
        fields = (
            "_display",
            "tellus",
            "richting",
            "naam_richting"
        )

    def get__display(self, obj):
        return str(obj)


class RichtingModelSerializer(serializers.ModelSerializer):
    """Serializer used by TelusDataCarsPerHourPerDaySerializer
    """

    class Meta:
        model = TellusRichting
        fields = '__all__'


class TellusDataCarsPerHourPerDaySerializer(HALSerializer):
    """
    Tellus Werkdag, Weekdag totalen
    """
    dataset = 'tellus_data'

    _display = serializers.SerializerMethodField()
    richting = RichtingModelSerializer()

    class Meta(object):
        model = TellusDataCarsPerHourPerDay
        fields = (
            "_display",
            "id",
            "tellus",
            "richting",
            "dag_uur_gemeten",
            "dag_type",
            "aantal"
        )

    def get__display(self, obj):
        return str(obj)
