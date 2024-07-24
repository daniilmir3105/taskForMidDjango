from django.db import models

class Tariff(models.Model):
    description = models.CharField(max_length=255)
    rate_per_unit = models.FloatField()  # цена за единицу ресурса/услуги
