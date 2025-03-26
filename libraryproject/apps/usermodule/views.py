from django.shortcuts import render

# Create your views here.
from .models import Student, Address
from django.db.models import Count

def city_count(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/city_count.html', {'city_stats': city_stats})
