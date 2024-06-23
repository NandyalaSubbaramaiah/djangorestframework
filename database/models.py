from django.db import models
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    roll_number = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=20, default='')
    
    def __self__(self):
        return self.user_name
    


