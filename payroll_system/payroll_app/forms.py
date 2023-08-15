from django import forms
from .models import Employee

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name']  # Add other fields as needed
