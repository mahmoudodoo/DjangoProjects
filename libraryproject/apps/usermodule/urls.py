from django.urls import path
from . import views

urlpatterns = [
    path('students/city_count/', views.city_count, name='students.city_count'),
    path('lab9/task2/', views.department_student_count, name='lab9.task2'),
    path('lab9/task3/', views.course_student_count, name='lab9.task3'),
    path('lab9/task4/', views.oldest_student_per_department, name='lab9.task4'),
    path('lab9/task5/', views.departments_more_than_two_students, name='lab9.task5'),
    
    # New URLs for Task 1
    path('students/', views.student_list, name='students.list'),
    path('students/create/', views.student_create, name='students.create'),
    path('students/update/<int:pk>/', views.student_update, name='students.update'),
    path('students/delete/<int:pk>/', views.student_delete, name='students.delete'),
    
     # New URLs for Task 2
    path('students2/', views.student2_list, name='students2.list'),
    path('students2/create/', views.student2_create, name='students2.create'),
    path('students2/update/<int:pk>/', views.student2_update, name='students2.update'),
    path('students2/delete/<int:pk>/', views.student2_delete, name='students2.delete'),
    
    #lab 11 task 3
    path('students/<int:student_id>/profile/create/', views.profile_create, name='students.profile.create'),
    path('students/<int:student_id>/profile/update/', views.profile_update, name='students.profile.update'),
    
    # lab 12 task 1
    path('register/', views.register, name='users.register'),
    path('login/', views.user_login, name='users.login'),
    path('logout/', views.user_logout, name='users.logout'),

]
