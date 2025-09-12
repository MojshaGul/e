from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as auth_login, 
    authenticate as auth_authenticate,
    logout as auth_logout
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth_app/register.html', {"form": form})

def login(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth_authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('task_list')
    else:
        form = AuthenticationForm()
        
    return render(request, 'auth_app/login.html', {"form": form})

def logout(request):
    auth_logout(request)
    return redirect('login_page')