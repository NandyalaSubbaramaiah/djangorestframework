from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    enrollment_date=models.DateField()
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
          
class person(models.Model):
    mobile_number=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.mobile_number}"
    
    