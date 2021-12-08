from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeCreateView,
    EmployeeDetailView,
    DepartmentListView,
    DepartmentUpdateView,
    DepartmentDeleteView,
    DepartmentCreateView,
    DepartmentDetailView,
)

urlpatterns = [
    path('employee/', EmployeeListView.as_view(), name='employee_list_url'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_create_url'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update_url'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete_url'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail_url'),
    path('department/', DepartmentListView.as_view(), name='department_list_url'),
    path('department/add/', DepartmentCreateView.as_view(), name='department_create_url'),
    path('department/<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department_update_url'),
    path('department/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete_url'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail_url'),
]
