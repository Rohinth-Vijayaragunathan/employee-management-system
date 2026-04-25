from django.shortcuts import render, redirect
from .models import Employee


def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def add_emp(request):
    if request.method == 'POST':
        Employee.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            department = request.POST['department'],
            salary = request.POST['salary']
        )
        return redirect('/')
    return render(request, 'add_emp.html')

def edit_emp(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == 'POST':
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.phone = request.POST['phone']
        emp.department = request.POST['department']
        emp.salary = request.POST['salary']
        emp.save()
        return redirect('/')
    return render(request, 'update_emp.html', {'emp' : emp})

def delete_emp(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')