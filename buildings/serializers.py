from rest_framework import serializers
from .models import Building, Apartment
from watermeters.serializers import WaterMeterSerializer

class ApartmentSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = '__all__'
