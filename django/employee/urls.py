from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    # Employee managemnet urls
    path('add/', views.CreateUpdateEmployee.as_view(), name="add_employee"),
    path('edit/<uuid:uuid>/', views.CreateUpdateEmployee.as_view(), name="edit_employee"),
    path('view/<uuid:uuid>/', views.ViewEmployee.as_view(), name="view_employee"),
    path('delete/<uuid:uuid>/', views.DeleteEmployee.as_view(), name="delete_employee"),
    path('list/', views.EmployeesList.as_view(), name="list_employee"),

    # Salary update url.
    path('update-salary/', views.CreateUpdateEmployeeSalary.as_view(), name="add_employee_salary"),
]