from django.urls import path
from myapp import views

urlpatterns = [
    path('create_employee/', views.create_employee, name='create_user'),
    # other paths...
]
