from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChartDataSerializer
from django.shortcuts import render

class ChartData(APIView):
    def get(self, request, format=None):
        data = {
            "xValues": ["Italy", "France", "Spain", "USA", "Argentina"],
            "yValues": [55, 49, 44, 24, 15],
            "barColors": ["red", "green", "blue", "orange", "brown"]
        }
        serializer = ChartDataSerializer(data)
        return Response(serializer.data)
    
   

def chart_view(request):
    return render(request, 'chart.html')