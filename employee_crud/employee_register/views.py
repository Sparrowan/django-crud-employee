from django.shortcuts import render,redirect
from .forms import EmployeeForm
from . models import employee

def employee_list(request):
    context = {'employee_list':employee.objects.all()}
    return render(request, "employee_register/employee_list.html",context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employe = employee.objects.get(pk=id) 
            form = EmployeeForm(instance=employe)
        return render(request, "employee_register/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employe = employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
        

def employee_delete(request,id):
    employe = employee.objects.get(pk=id)
    employe.delete()
    return redirect('/employee/list')
 