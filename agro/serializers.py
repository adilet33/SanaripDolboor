from rest_framework.serializers import ModelSerializer
from .models import *


class CultureSerializer(ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class CultureSerializer(ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class FarmerSerializer(ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class PlotSerializer(ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'


class SeasonSerializer(ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
