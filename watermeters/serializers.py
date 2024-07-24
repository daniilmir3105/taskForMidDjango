from rest_framework import serializers
from .models import WaterMeter, WaterReading

class WaterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterReading
        fields = '__all__'

class WaterMeterSerializer(serializers.ModelSerializer):
    readings = WaterReadingSerializer(many=True, read_only=True)

    class Meta:
        model = WaterMeter
        fields = '__all__'
