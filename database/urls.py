from django.urls import path
from myapp import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    # other paths...
]
