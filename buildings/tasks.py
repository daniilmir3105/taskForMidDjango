from celery import shared_task
from .utils import calculate_rent

@shared_task
def calculate_rent_task(building_id, month):
    calculate_rent(building_id, month)
