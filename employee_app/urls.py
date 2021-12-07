from django.urls import path
from .views import EmployeeListView, EmployeeUpdateView

urlpatterns = [
    path('employee/', EmployeeListView.as_view(), name='employee_list_url'),
    path('employee/edit/', EmployeeUpdateView.as_view(), name='employee_update_url')
]
