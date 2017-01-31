from rest_framework import serializers
from datasets.tellus_data.models import Tellus, LengteCategorie, SnelheidsCategorie, TellusData


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
    class Meta:
        model = TellusData
        fields = '__all__'
