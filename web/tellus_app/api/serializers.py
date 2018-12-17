from rest_framework import serializers

from datapunt_api.rest import HALSerializer

from datasets.tellus_data.models import LengteInterval, Telling, TellusDataCarsPerHourPerDay, SnelheidsInterval, \
    SnelheidsCategorie, Meetlocatie, MeetraaiCategorie, ValidatieCategorie, RepresentatiefCategorie, \
    TellusDataCarsPerHourLength, TellusDataCarsPerHourSpeed
from datasets.tellus_data.models import Tellus
from datasets.tellus_data.models import TelRichting


class MeetlocatieSerializer(HALSerializer):
    dataset = 'tellus_data'

    class Meta(object):
        model = Meetlocatie
        fields = (
            "id",
            "name"
        )


class LengteIntervalSerializer(HALSerializer):
    """
    Lengte interval.
    """
    dataset = 'tellus_data'

    class Meta(object):
        model = LengteInterval
        fields = (
            "id",
            "label",
            "min_cm",
            "max_cm"
        )


class SnelheidsIntervalSerializer(HALSerializer):
    """
    Snelheids interval.
    """
    dataset = 'tellus_data'

    class Meta(object):
        model = SnelheidsInterval
        fields = (
            "id",
            "label",
            "min_kmph",
            "max_kmph"
        )


class SnelheidsCategorieSerializer(HALSerializer):
    dataset = 'tellus_data'

    interval = SnelheidsIntervalSerializer()

    class Meta(object):
        model = SnelheidsCategorie
        fields = (
            "categorie",
            "index",
            "interval",
        )


class RepresentatiefCategorieSerializer(HALSerializer):
    dataset = 'tellus_data'

    class Meta(object):
        model = RepresentatiefCategorie
        fields = (
            "id",
            "label"
        )


class ValidatieCategorieSerializer(HALSerializer):
    dataset = 'tellus_data'

    class Meta(object):
        model = ValidatieCategorie
        fields = (
            "id",
            "label"
        )


class MeetraaiCategorieSerializer(HALSerializer):
    dataset = 'tellus_data'

    class Meta(object):
        model = MeetraaiCategorie
        fields = (
            "id",
            "label"
        )


class TelRichtingSerializer(HALSerializer):
    """
    Tellus Werkdag, Weekdag totalen
    """
    dataset = 'tellus_data'
    _display = serializers.SerializerMethodField()
    tellus = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta(object):
        model = TelRichting
        fields = (
            "_display",
            "tellus",
            "richting",
            "naam",
            "zijstraat"
        )

    def get__display(self, obj):
        return str(obj)


class TellusSerializer(HALSerializer):
    """
    Tellus details
    """
    dataset = 'tellus_data'
    _display = serializers.SerializerMethodField()
    meetlocatie = MeetlocatieSerializer()
    tel_richtingen = TelRichtingSerializer(many=True)

    class Meta(object):
        model = Tellus
        fields = (
            "_display",
            "id",
            "objnr_vor",
            "objnr_leverancier",
            "snelheids_categorie",
            "meetlocatie",
            "tel_richtingen",
            "latitude",
            "longitude",
            "rijksdriehoek_x",
            "rijksdriehoek_y",
            "geometrie",
        )

    def get__display(self, obj):
        return str(obj)


class TellingSerializer(HALSerializer):
    """
    Tellus tellingen.
    """
    dataset = 'tellus_data'
    _display = serializers.SerializerMethodField()
    validatie_categorie = ValidatieCategorieSerializer()
    representatief_categorie = RepresentatiefCategorieSerializer()
    meetraai_categorie = MeetraaiCategorieSerializer()

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
            "meetraai_categorie"
        )

    def get__display(self, obj):
        return str(obj)


class TellusModelSerializer(serializers.ModelSerializer):
    """
    Serializer used by TelusDataCarsPerHourPerDaySerializer
    """

    class Meta:
        model = Tellus
        fields = (
            "id",
            "standplaats"
        )


class TellusDataCarsPerHourPerDaySerializer(HALSerializer):
    """
    Tellus Werkdag, Weekdag totalen
    """
    dataset = 'tellus_data'
    tellus = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta(object):
        model = TellusDataCarsPerHourPerDay
        fields = (
            "id",
            "tellus",
            "richting_id",
            "dag_uur",
            "dag_type",
            "aantal"
        )


class TellusDataCarsPerHourLengthSerializer(HALSerializer):
    """
    Tellus Werkdag, Weekdag totalen
    """
    dataset = 'tellus_data'
    tellus = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta(object):
        model = TellusDataCarsPerHourLength
        fields = (
            "id",
            "tellus",
            "richting_id",
            "dag_uur",
            "dag_type",
            "lengte_interval_id",
            "label",
            "aantal"
        )


class TellusDataCarsPerHourSpeedSerializer(HALSerializer):
    """
    Tellus Werkdag, Weekdag totalen
    """
    dataset = 'tellus_data'
    tellus = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta(object):
        model = TellusDataCarsPerHourSpeed
        fields = (
            "id",
            "tellus",
            "richting_id",
            "dag_uur",
            "dag_type",
            "snelheids_interval_id",
            "label",
            "aantal"
        )
