from rest_framework import serializers
from datasets.tellus_data.models import Tellus, LengteCategorie, SnelheidsCategorie, TellusData
import json

class TellusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tellus
        fields = '__all__'


class LengteCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = LengteCategorie
        fields = '__all__'



class SnelheidsCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnelheidsCategorie
        fields = '__all__'



class TellusDataSerializer(serializers.ModelSerializer):
    meet_resultaten = serializers.SerializerMethodField()

    class Meta:
        model = TellusData
        exclude = ('data', )

    def get_meet_resultaten(self, obj):
        return json.loads(obj.data)
