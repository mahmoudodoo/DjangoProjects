from django.urls import path
from . import views
from apps.usermodule import views as user_views

urlpatterns = [
    # All existing URLs remain unchanged
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page, name='books.links'),
    path('html5/text/formatting/', views.text_formatting_page, name='books.text_formatting'),
    path('html5/listing/', views.listing_page, name='books.listing'),
    path('html5/tables/', views.tables_page, name='books.tables'),
    path('search/', views.search_books, name='books.search'),
    path('simple/query/', views.simple_query, name='books.simple_query'),
    path('complex/query/', views.complex_query, name='books.complex_query'),
    path('lab8/task1/', views.task1, name='lab8.task1'),
    path('lab8/task2/', views.task2, name='lab8.task2'),
    path('lab8/task3/', views.task3, name='lab8.task3'),
    path('lab8/task4/', views.task4, name='lab8.task4'),
    path('lab8/task5/', views.task5, name='lab8.task5'),
    path('lab9_part1/listbooks/', views.list_books, name='lab9_part1.listbooks'),
    path('lab9_part1/addbook/', views.add_book, name='lab9_part1.addbook'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='lab9_part1.editbook'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='lab9_part1.deletebook'),
    path('lab9_part2/listbooks/', views.list_books_with_forms, name='lab9_part2.listbooks'),
    path('lab9_part2/addbook/', views.add_book_with_form, name='lab9_part2.addbook'),
    path('lab9_part2/editbook/<int:id>/', views.edit_book_with_form, name='lab9_part2.editbook'),
    path('lab9_part2/deletebook/<int:id>/', views.delete_book_with_form, name='lab9_part2.deletebook'),

    # New URLs for Lab 9 tasks - mounted under /books/
    path('lab9/task2/', user_views.department_student_count, name='lab9.task2'),
    path('lab9/task3/', user_views.course_student_count, name='lab9.task3'),
    path('lab9/task4/', user_views.oldest_student_per_department, name='lab9.task4'),
    path('lab9/task5/', user_views.departments_more_than_two_students, name='lab9.task5'),
]
