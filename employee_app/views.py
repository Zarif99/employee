from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Department, Employee
from .forms import DepartmentForm


class EmployeeUpdateView(UpdateView):
    model = Employee
    context_object_name = 'employee'


class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
