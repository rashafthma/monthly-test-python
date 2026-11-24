from re import search

from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def Employee_list(request):
    employees=Employee.objects.all()
    return render(request,'employee_list.html',{"employees":employees})

def AddEmployee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('employee_list')
    else:
        form=EmployeeForm()
    return render(request,'add_employee.html',{"form":form})

def EditEmployee(request,id):
    employee=get_object_or_404(Employee,id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')
    else:
        form=EmployeeForm(instance=employee)
    return render(request,'edit_employee.html',{"form":form})

def DeleteEmployee(request,id):
    employee=get_object_or_404(Employee,id=id)
    employee.delete()
    return redirect('employee_list')

def SearchEmployee(request):
    employees=Employee.objects.all()

    search=request.GET.get('search')
    if search:
        employees=employees.filter(name__icontains=search)

    department=request.GET.get('department')
    if department:  
        employees=employees.filter(department__icontains=department)

    return render(request,'employee_list.html',{"employees1":employees})