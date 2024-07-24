from django.db import models

class Building(models.Model):
    address = models.CharField(max_length=255)

class Apartment(models.Model):
    building = models.ForeignKey(Building, related_name='apartments', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    area = models.FloatField()  # площадь квартиры

class Payment(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='payments', on_delete=models.CASCADE)
    month = models.DateField()
    water_supply_cost = models.FloatField()
    maintenance_cost = models.FloatField()
    total_cost = models.FloatField()
