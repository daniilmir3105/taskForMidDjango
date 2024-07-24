from rest_framework import viewsets
from .models import Building
from .serializers import BuildingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import calculate_rent_task
from datetime import datetime

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class CalculateRentView(APIView):
    def post(self, request, building_id):
        month = request.data.get('month')
        month = datetime.strptime(month, '%Y-%m-%d')
        calculate_rent_task.delay(building_id, month)
        return Response({"status": "Calculation started"})
