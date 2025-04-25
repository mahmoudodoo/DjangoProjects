from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Address, Department, Course,Card,Student2,StudentProfile
from django.db.models import Count, Min
from .forms import StudentForm, AddressForm,Student2Form,StudentProfileForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('students.list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'usermodule/login.html', {'form': form})



def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('users.login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('students.list')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegisterForm()
    return render(request, 'usermodule/register.html', {'form': form})

# Existing views (DO NOT REMOVE)
def city_count(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/city_count.html', {'city_stats': city_stats})

# New views for Lab 9
def department_student_count(request):
    departments = Department.objects.annotate(student_count=Count('students'))
    return render(request, 'usermodule/department_count.html', {'departments': departments})

def course_student_count(request):
    courses = Course.objects.annotate(student_count=Count('students'))
    return render(request, 'usermodule/course_count.html', {'courses': courses})

def oldest_student_per_department(request):
    departments = Department.objects.annotate(
        oldest_student_id=Min('students__id')
    ).prefetch_related('students')
    
    dept_data = []
    for dept in departments:
        oldest_student = dept.students.filter(id=dept.oldest_student_id).first()
        dept_data.append({
            'department': dept,
            'oldest_student': oldest_student
        })
    
    return render(request, 'usermodule/oldest_student.html', {'dept_data': dept_data})

def departments_more_than_two_students(request):
    departments = Department.objects.annotate(
        student_count=Count('students')
    ).filter(
        student_count__gt=2
    ).order_by('-student_count')
    
    return render(request, 'usermodule/departments_more_than_two.html', {'departments': departments})



# Add these new views for Task 1
def student_list(request):
    students = Student.objects.select_related('address').all()
    return render(request, 'usermodule/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students.list')
    else:
        form = StudentForm()
    return render(request, 'usermodule/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students.list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students.list')
    return render(request, 'usermodule/student_confirm_delete.html', {'student': student})

# Add these new views for Task 2

def student2_list(request):
    students = Student2.objects.prefetch_related('addresses').all()
    return render(request, 'usermodule/student2_list.html', {'students': students})

@login_required
def student2_create(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            student = form.save()
            # Manually save the many-to-many relationship
            student.addresses.set(form.cleaned_data['addresses'])
            messages.success(request, 'Student created successfully!')
            return redirect('students2.list')
    else:
        form = Student2Form()
    return render(request, 'usermodule/student2_form.html', {'form': form})

def student2_update(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            # Manually save the many-to-many relationship
            student.addresses.set(form.cleaned_data['addresses'])
            messages.success(request, 'Student updated successfully!')
            return redirect('students2.list')
    else:
        form = Student2Form(instance=student)
        # Initialize the addresses for the form
        form.fields['addresses'].initial = student.addresses.all()
    return render(request, 'usermodule/student2_form.html', {'form': form})

def student2_delete(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students2.list')
    return render(request, 'usermodule/student2_confirm_delete.html', {'student': student})


# Add these new views for Task 3
def profile_create(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.student = student
            profile.save()
            return redirect('students.list')
    else:
        form = StudentProfileForm()
    return render(request, 'usermodule/profile_form.html', {'form': form, 'student': student})

def profile_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    profile = get_object_or_404(StudentProfile, student=student)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('students.list')
    else:
        form = StudentProfileForm(instance=profile)
    return render(request, 'usermodule/profile_form.html', {'form': form, 'student': student})