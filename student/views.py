from rest_framework import generics
from .models import student, person
from .serializers import StudentSerializer, personSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    
class PersonListCreate(generics.ListCreateAPIView):
    queryset=person.objects.all()
    serializer_class= personSerializer
        