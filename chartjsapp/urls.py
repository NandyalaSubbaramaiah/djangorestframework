from django.urls import path
from .views import chart_view, ChartData

urlpatterns = [
    path('chart/', chart_view, name='chart-view'),
    path('chartjsapp/chart-data/', ChartData.as_view(), name='chart-data'),
]