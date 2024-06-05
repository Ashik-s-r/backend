from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import medicineForm
from .models import medicine
from django.contrib.auth.decorators import user_passes_test,login_required

def hlo(request):
    return render(request,'home.html')

 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home1')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form': form})

def  user_check(user):
    return user.username.endswith('@example.com')

@login_required(login_url='/login/')
@user_passes_test(user_check,login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = medicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form =medicineForm()
    return render(request, 'create.html', {'form': form})

def  user_check(user):
    return user.username.endswith('@example.com')

@login_required(login_url='/login/')
@user_passes_test(user_check,login_url='/login/')
def read(request):
    list=medicine.objects.all()
    return render(request,'retrieve.html',{'list':list})

def  user_check(user):
    return user.username.endswith('@example.com')

@login_required(login_url='/login/')
@user_passes_test(user_check,login_url='/login/')
def update(request, id):
    medicine1 = medicine.objects.get(pk=id)
    if request.method == 'POST':
        form = medicineForm(request.POST,instance=medicine1)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form =medicineForm(instance=medicine1)           
    return render(request, 'update.html', {'form': form})

def  user_check(user):
    return user.username.endswith('@example.com')

@login_required(login_url='/login/')
@user_passes_test(user_check,login_url='/login/')
def delete1(request,id):
    med=medicine.objects.get(pk=id)  
    if request.method == 'POST':
        med.delete()
        return redirect('read')
    
    return render(request,'delete.html',{'med':med})


from django.shortcuts import render
from .models import medicine

def search(request):
    query = request.GET.get('query')
    if query:
        medicines = medicine.objects.filter(MedicineName__iexact=query)
    else:
        medicines = medicine.objects.none()
    return render(request, 'search.html', {'medicines': medicines})









