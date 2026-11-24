from django.urls import path
from .views import Employee_list,AddEmployee,EditEmployee,DeleteEmployee

urlpatterns = [
    path('', Employee_list, name='employee_list'),
    path('add/', AddEmployee, name='add_employee'),
    path('edit/<int:id>/', EditEmployee, name='edit_employee'), 
    path('delete/<int:id>/', DeleteEmployee, name='delete_employee'),
]