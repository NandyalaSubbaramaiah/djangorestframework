from django.urls import path
from .views import pie_chart, chart_view

urlpatterns = [
    path('pie-chart/', pie_chart, name='pie_chart'),
]


urlpatterns = [
    path('chart/', chart_view, name='chart-view'),
]

urlpatterns = [
    path('chart/', chart_view, name='chart-view'),
]


