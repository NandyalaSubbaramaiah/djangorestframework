from django.db import models
# Create your models here.
class Employee(models.Model):
    EmployeeID=models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    AddressLine=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, default='')
    
    def __self__(self):
        return self.Email
    


