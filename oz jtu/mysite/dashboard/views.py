from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_required_decorator(f):
    return login_required(f, login_url='login')


@login_required_decorator
def dashboard_page(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    return render(request, 'dashboard/index.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')
