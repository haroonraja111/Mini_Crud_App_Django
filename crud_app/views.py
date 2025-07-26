from django.shortcuts import render
from .models import Employee
from django.shortcuts import redirect

# Create your views here.

def create_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        father_name = request.POST['father_name']
        position = request.POST['position']
        salary = request.POST['salary']
        Employee.objects.create(name=name, father_name=father_name, position=position, salary=salary)
        return redirect('employee_list')
    return render(request, 'crud_app/create_employee.html')

def employee_list(request):
    employees = Employee.objects.all
    return render(request, 'crud_app/employee_list.html', {'employees': employees})

def update_employee(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    if request.method == 'POST':
        employee.name = request.POST.get('name', employee.name)
        employee.father_name = request.POST.get('father_name', employee.father_name)
        employee.position = request.POST.get('position', employee.position)
        employee.salary = request.POST.get('salary', employee.salary)
        employee.save()
        return redirect('employee_list')
    context = {'employee': employee}
    return render(request, 'crud_app/update_employee.html', context)

def delete_employee(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    context = { 
        'employee': employee
    }
    return render(request, 'crud_app/delete_employee.html', context)

