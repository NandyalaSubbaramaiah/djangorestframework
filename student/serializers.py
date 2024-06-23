from rest_framework import serializers
from .models import student, person

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
class personSerializer(serializers.ModelSerializer):
    class Meta:
        model=person
        fields='__all__'        