from django.db import models
from buildings.models import Apartment

class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='water_meters', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50)

class WaterReading(models.Model):
    meter = models.ForeignKey(WaterMeter, related_name='readings', on_delete=models.CASCADE)
    date = models.DateField()
    reading = models.FloatField()  # показания счётчика
