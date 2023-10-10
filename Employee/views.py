from django.shortcuts import render
from salary.models import Employee


def home1(request):
    employees=Employee.objects.all()
    context={
        'employees':employees,
    }
    print(employees)
    return render(request,'home1.html',context)

def employee_detail(request):
    employees=Employee.objects.all()
    context={
        'employees':employees,
    }

    return render(request,'employee_detail.html',context)


