from django.urls import path
from . import views

urlpatterns = [
    # Existing URL (DO NOT REMOVE)
    path('students/city_count/', views.city_count, name='students.city_count'),
    
    # New URLs for Lab 9
    path('lab9/task2/', views.department_student_count, name='lab9.task2'),
    path('lab9/task3/', views.course_student_count, name='lab9.task3'),
    path('lab9/task4/', views.oldest_student_per_department, name='lab9.task4'),
    path('lab9/task5/', views.departments_more_than_two_students, name='lab9.task5'),
]
