from django import forms
from .models import Student, Address,Student2,StudentProfile,Address2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
        
        
class Student2Form(forms.ModelForm):
    new_address = forms.CharField(
        required=False,
        label="Add new address",
        help_text="Enter a city name to create new address"
    )
    
    class Meta:
        model = Student2
        fields = ['name', 'age']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add addresses field dynamically
        self.fields['addresses'] = forms.ModelMultipleChoiceField(
            queryset=Address2.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
        if self.instance.pk:
            self.fields['addresses'].initial = self.instance.addresses.all()
    
    def clean(self):
        cleaned_data = super().clean()
        new_address = cleaned_data.get('new_address')
        addresses = cleaned_data.get('addresses', [])
        
        if not addresses and not new_address:
            raise forms.ValidationError("You must select at least one existing address or enter a new one.")
        
        return cleaned_data
    
    def save(self, commit=True):
        student = super().save(commit=commit)
        addresses = list(self.cleaned_data.get('addresses', []))  # Convert to list
        
        new_address = self.cleaned_data.get('new_address')
        if new_address:
            address, created = Address2.objects.get_or_create(city=new_address)
            addresses.append(address)  # Now we can append to the list
        
        if commit:
            student.addresses.set(addresses)  # Use set() for many-to-many
        
        return student
    
    
    
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['profile_picture', 'bio']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class LoginForm(AuthenticationForm):
    pass