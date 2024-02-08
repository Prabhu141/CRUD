from django.shortcuts import render, redirect
from .models import company
from .forms import companyform
# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'index.html')


def create(request):
    if request.method=="POST":
        employee_id = request.POST['employee_id']
        employee_name = request.POST['employee_name']
        employee_phone = request.POST['employee_phone']
        obj = company.objects.create(employee_id=employee_id,employee_name=employee_name,employee_phone=employee_phone)
        obj.save()
        return redirect('/')
    
def retrieve(request):
    data=company.objects.all()
    return render(request,'retrieve.html',{'data':data})

def edit(request,id):
    details=company.objects.get(id=id)
    return render(request,'edit.html',{'details':details})

def update(request,id):
    object=company.objects.get(id=id)
    form=companyform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=company.objects.all()
        return redirect('retrieve')

def delete(request,id):
    company.objects.filter(id=id).delete()
    return redirect('retrieve')


