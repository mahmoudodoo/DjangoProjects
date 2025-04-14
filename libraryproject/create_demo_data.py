import os
import django
from faker import Faker
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()

from apps.usermodule.models import Address, Student, Card, Department, Course
from apps.bookmodule.models import Book

fake = Faker()

def clear_existing_data():
    """Delete all existing data from all tables"""
    print("Clearing existing data...")
    Book.objects.all().delete()
    Student.objects.all().delete()
    Card.objects.all().delete()
    Department.objects.all().delete()
    Course.objects.all().delete()
    Address.objects.all().delete()
    print("All existing data cleared.")

def create_departments():
    departments = [
        "Computer Science",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Mathematics",
        "Physics",
        "Biology",
        "Chemistry",
        "Economics",
        "Business Administration",
        "Psychology"
    ]
    dept_objects = []
    for name in departments:
        dept = Department.objects.create(name=name)
        dept_objects.append(dept)
        print(f"Created department: {dept}")
    return dept_objects

def create_courses():
    courses = [
        {"title": "Introduction to Programming", "code": 101},
        {"title": "Data Structures", "code": 201},
        {"title": "Algorithms", "code": 301},
        {"title": "Database Systems", "code": 202},
        {"title": "Operating Systems", "code": 302},
        {"title": "Computer Networks", "code": 303},
        {"title": "Artificial Intelligence", "code": 401},
        {"title": "Machine Learning", "code": 402},
        {"title": "Calculus I", "code": 111},
        {"title": "Linear Algebra", "code": 112}
    ]
    course_objects = []
    for course in courses:
        crs = Course.objects.create(title=course["title"], code=course["code"])
        course_objects.append(crs)
        print(f"Created course: {crs}")
    return course_objects

def create_addresses():
    addresses = []
    for _ in range(10):
        address = Address.objects.create(
            city=fake.city()
        )
        addresses.append(address)
        print(f"Created address: {address}")
    return addresses

def create_cards():
    cards = []
    for i in range(50):
        card = Card.objects.create(
            card_number=100000 + i  # Ensure unique card numbers
        )
        cards.append(card)
        print(f"Created card: {card}")
    return cards

def create_books():
    books = []
    for i in range(20):
        book = Book.objects.create(
            title=fake.catch_phrase(),
            author=fake.name(),
            price=round(random.uniform(10, 100), 2),
            edition=random.randint(1, 5)
        )
        books.append(book)
        print(f"Created book: {book}")
    return books

def create_students(addresses, cards, departments, courses):
    for i in range(50):
        student = Student.objects.create(
            name=fake.name(),
            age=fake.random_int(min=18, max=25),
            address=random.choice(addresses),
            card=cards[i],
            department=random.choice(departments)
        )
        # Assign 3-5 random courses to each student
        student.courses.set(random.sample(courses, k=random.randint(3, 5)))
        print(f"Created student {i+1}: {student}")

def create_demo_data():
    clear_existing_data()
    
    print("\nCreating departments...")
    departments = create_departments()
    
    print("\nCreating courses...")
    courses = create_courses()
    
    print("\nCreating addresses...")
    addresses = create_addresses()
    
    print("\nCreating cards...")
    cards = create_cards()
    
    print("\nCreating books...")
    create_books()
    
    print("\nCreating students with relationships...")
    create_students(addresses, cards, departments, courses)

if __name__ == '__main__':
    print("Starting demo data creation...")
    create_demo_data()
    print("\nDemo data creation complete!")
