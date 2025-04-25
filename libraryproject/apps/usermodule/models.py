from django.db import models
from django.core.validators import FileExtensionValidator

# Existing models (DO NOT REMOVE)
class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

# New models for Lab 9
class Card(models.Model):
    card_number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.card_number)

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.title} ({self.code})"

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    card = models.OneToOneField(
        Card,
        on_delete=models.PROTECT,  # Prevents card deletion if linked to student
        related_name='student',
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,  # Deletes students when department is deleted
        related_name='students',
        null=True,
        blank=True
    )
    courses = models.ManyToManyField(
        Course,
        related_name='students',
        blank=True
    )

    def __str__(self):
        return self.name
    



class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2, related_name='students')
    
    def __str__(self):
        return self.name



class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.student.name}'s Profile"
    
    @property
    def picture_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        return '/static/avatar.png'