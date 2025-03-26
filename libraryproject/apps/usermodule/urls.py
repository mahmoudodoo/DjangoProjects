from django.urls import path
from . import views
urlpatterns = [
     path('students/city_count/', views.city_count, name='students.city_count'),
]
