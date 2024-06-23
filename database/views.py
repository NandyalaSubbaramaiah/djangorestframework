from django.shortcuts import render
from myapp.models import User

def create_user(request):
    # Assuming you have already imported User model and created an instance
    user = User(first_name='nandyala', last_name='subbu', user_name='subbu0063', roll_number=1)
    user.save()
    
    return render(request, 'database/success.html')
