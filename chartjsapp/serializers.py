from rest_framework import serializers

class ChartDataSerializer(serializers.Serializer):
      xValues=serializers.ListField(child=serializers.CharField())
      yValues=serializers.ListField(child=serializers.IntegerField())
      barColors=serializers.ListField(child=serializers.CharField())
      