from .models import Apartment, Payment
from tariffs.models import Tariff
from watermeters.models import WaterReading


def calculate_rent(building_id, month):
    apartments = Apartment.objects.filter(building_id=building_id)
    water_tariff = Tariff.objects.get(description='Water')
    maintenance_tariff = Tariff.objects.get(description='Maintenance')

    for apartment in apartments:
        water_meters = apartment.water_meters.all()
        water_cost = 0

        for meter in water_meters:
            readings = WaterReading.objects.filter(meter=meter, date__month=month.month, date__year=month.year)
            if readings.count() == 2:
                current_reading, previous_reading = readings.order_by('date')
                water_cost += (current_reading.reading - previous_reading.reading) * water_tariff.rate_per_unit

        maintenance_cost = apartment.area * maintenance_tariff.rate_per_unit
        total_cost = water_cost + maintenance_cost

        Payment.objects.create(
            apartment=apartment,
            month=month,
            water_supply_cost=water_cost,
            maintenance_cost=maintenance_cost,
            total_cost=total_cost
        )
