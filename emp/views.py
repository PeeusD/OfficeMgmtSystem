from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html' )


def all_emp(request):
    emps= Employee.objects.all()
    context={'emps':emps}
    # print(context)
    return render(request,'view_all_emp.html', context=context )


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        # loc = request.POST['location']
        role = int(request.POST['role'])
        # hire_dt = request.POST['dire_dt']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, 
        bonus=bonus, phone=phone,  dept_id=dept, role_id=role, hire_date= datetime.now())
        new_emp.save()
        return HttpResponse('emp added successfully!')
    
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    


    else:
        return HttpResponse('Exception Occured!!')
    



def remove_emp(request, emp_id=None):
    if emp_id:
        try:
            rem_emp = Employee.objects.get(id=emp_id)
            rem_emp.delete()
            return HttpResponse("employee deleted successfully!")
        except:
            return HttpResponse("Not exis...Please enter again emp id")
    emps= Employee.objects.all()
  
    context = {'emps': emps}
    return render(request,'remove_emp.html', context=context)



def filter_emp(request):
    if request.method=='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context={'emps': emps}
        return render(request,'view_all_emp.html' , context=context)
    elif request.method=='GET':
        return render(request,'filter_emp.html' )
    else:
        return HttpResponse("Exception occured!" )
