from django.db import models

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
    address = models.ForeignKey(Address, on_delete=models.CASCADE)  # Existing relationship
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