from django.urls import path
from . import views
urlpatterns = [
    path('student/', views.StudentListCreate.as_view(), name='student-list-create'),
    path('student/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view(), name='student-detail'),
    path('person/', views.PersonListCreate.as_view(), name='person-list-create'), 
]