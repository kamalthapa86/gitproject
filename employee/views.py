from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmployeeForm
from .models import Employee
# Create your views here.


def home(request):
    if request.method == 'POST':
        forms = EmployeeForm(request.POST)
        if forms.is_valid():
            fn = forms.cleaned_data['first_name']
            ln = forms.cleaned_data['last_name']
            db = forms.cleaned_data['dob']
            data = Employee(first_name = fn, last_name = ln, dob = db)
            data.save()
            return redirect('/success/')
    else:
        all_emp = Employee.objects.all()
        forms = EmployeeForm()
        return render(request,'employee/home.html',context={'forms':forms, 'employees':all_emp})


def success(request):
    return render(request, 'employee/success.html',{})