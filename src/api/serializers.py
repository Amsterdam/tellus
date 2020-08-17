from rest_framework import serializers

from datapunt_api.rest import HALSerializer

from datasets.tellus_data.models import (
    LengteInterval,
    Telling,
    SnelheidsInterval,
    SnelheidsCategorie,
    Meetlocatie,
    MeetraaiCategorie,
    ValidatieCategorie,
    RepresentatiefCategorie,
)
from datasets.tellus_data.models import Tellus
from datasets.tellus_data.models import TelRichting


class MeetlocatieSerializer(HALSerializer):
    dataset = "tellus_data"

    class Meta(object):
        model = Meetlocatie
        fields = ("id", "name")


class LengteIntervalSerializer(HALSerializer):
    """
    Lengte interval.
    """

    dataset = "tellus_data"

    class Meta(object):
        model = LengteInterval
        fields = ("id", "label", "min_cm", "max_cm")


class SnelheidsIntervalSerializer(HALSerializer):
    """
    Snelheids interval.
    """

    dataset = "tellus_data"

    class Meta(object):
        model = SnelheidsInterval
        fields = ("id", "label", "min_kmph", "max_kmph")


class SnelheidsCategorieSerializer(HALSerializer):
    dataset = "tellus_data"

    interval = SnelheidsIntervalSerializer()

    class Meta(object):
        model = SnelheidsCategorie
        fields = (
            "categorie",
            "index",
            "interval",
        )


class RepresentatiefCategorieSerializer(HALSerializer):
    dataset = "tellus_data"

    class Meta(object):
        model = RepresentatiefCategorie
        fields = ("id", "label")


class ValidatieCategorieSerializer(HALSerializer):
    dataset = "tellus_data"

    class Meta(object):
        model = ValidatieCategorie
        fields = ("id", "label")


class MeetraaiCategorieSerializer(HALSerializer):
    dataset = "tellus_data"

    class Meta(object):
        model = MeetraaiCategorie
        fields = ("id", "label")


class TellusSerializer(HALSerializer):
    """
    Tellus details
    """

    dataset = "tellus_data"
    _display = serializers.SerializerMethodField()
    meetlocatie = MeetlocatieSerializer()

    class Meta(object):
        model = Tellus
        fields = (
            "_display",
            "id",
            "objnr_vor",
            "objnr_leverancier",
            "snelheids_categorie",
            "meetlocatie",
            "latitude",
            "longitude",
            "rijksdriehoek_x",
            "rijksdriehoek_y",
            "geometrie",
        )

    def get__display(self, obj):
        return str(obj)


class TelRichtingSerializer(HALSerializer):
    """
    Tel richting
    """

    dataset = "tellus_data"
    _display = serializers.SerializerMethodField()
    tellus = TellusSerializer()

    class Meta(object):
        model = TelRichting
        fields = ("_display", "id", "tellus", "richting", "naam", "zijstraat")

    def get__display(self, obj):
        return str(obj)


class TellingSerializer(HALSerializer):
    """
    Tellus tellingen.
    """

    dataset = "tellus_data"
    _display = serializers.SerializerMethodField()
    tel_richting = serializers.PrimaryKeyRelatedField(read_only=True)
    lengte_interval = serializers.PrimaryKeyRelatedField(read_only=True)
    snelheids_interval = serializers.PrimaryKeyRelatedField(read_only=True)
    validatie_categorie = serializers.PrimaryKeyRelatedField(read_only=True)
    representatief_categorie = serializers.PrimaryKeyRelatedField(read_only=True)
    meetraai_categorie = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta(object):
        model = Telling

        fields = (
            "_display",
            "tijd_van",
            "tijd_tot",
            "aantal",
            "tel_richting",
            "snelheids_interval",
            "lengte_interval",
            "validatie_categorie",
            "representatief_categorie",
            "meetraai_categorie",
        )

    def get__display(self, obj):
        return str(obj)
