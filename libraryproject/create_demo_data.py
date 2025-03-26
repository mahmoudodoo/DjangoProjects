import os
import django
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()

from apps.usermodule.models import Address, Student 

fake = Faker()

def create_demo_data():
    # Create 10 addresses first
    addresses = []
    for _ in range(10):
        address = Address.objects.create(
            city=fake.city()
        )
        addresses.append(address)
        print(f"Created address: {address}")
    
    # Create 50 students with random addresses
    for i in range(50):
        student = Student.objects.create(
            name=fake.name(),
            age=fake.random_int(min=18, max=25),  # Assuming college age students
            address=fake.random_element(addresses)
        )
        print(f"Created student {i+1}: {student}")

if __name__ == '__main__':
    print("Creating demo data...")
    create_demo_data()
    print("Demo data creation complete!")