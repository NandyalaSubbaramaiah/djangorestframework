from django.shortcuts import render
from myapp.models import User

def create_employee(request):
    # Assuming you have already imported User model and created an instance
     employee= Employee(EmployeeID='1',FirstName  ='nandyala', LastName ='subbu', Email  ='subbu0063', AddressLine =1,City ='Tirupati')
     employee.save()
     return render(request, 'database/success.html')
