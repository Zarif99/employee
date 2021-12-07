from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_app/employee_create.html'
    fields = ('first_name', 'last_name', 'age', 'department', 'programming_language')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_app/employee_detail.html'
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee_app/employee_update.html'
    fields = ('first_name', 'last_name', 'age', 'department', 'programming_language')


class EmployeeDeleteView(DeleteView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee_app/employee_delete.html'
