from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['first_name','last_name','dob']
        labels = {'first_name':'First Name ',
                  'last_name':'Last Name ',
                  'dob':'Date of Birth :'}
        widgets = {'dob':forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'})}