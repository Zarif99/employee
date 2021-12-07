from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeCreateView
)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list_url'),
    path('add/', EmployeeCreateView.as_view(), name='employee_create_url'),
    path('<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update_url'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete_url'),
]
