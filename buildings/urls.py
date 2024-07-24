from rest_framework.routers import DefaultRouter
from .views import BuildingViewSet
from django.urls import path, include
from .views import CalculateRentView


router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('buildings/', include(router.urls)),
    path('calculate_rent/<int:building_id>/', CalculateRentView.as_view()),
]
