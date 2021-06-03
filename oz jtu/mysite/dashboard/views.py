from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import servise
from .forms import *
from univer.models import Menu, Basic_menu, Contact, Category, Teacher, News


def login_required_decorator(f):
    return login_required(f, login_url='login')


def dashboard_page(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    return render(request, 'dashboard/index.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def menu_list(request):
    menus = servise.get_menu()
    ctx = {
        "menus": menus,
    }
    return render(request, 'dashboard/menu/list.html', ctx)


def menu_create(request):
    model = Menu()
    form = MenuForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('menu_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/menu/form.html', ctx)


def menu_edit(request, pk):
    model = Menu.objects.get(id=pk)
    form = MenuForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('menu_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/menu/form.html', ctx)


def menu_delete(request, pk):
    model = Menu.objects.get(id=pk)
    model.delete()
    return redirect('menu_list')


def basic_list(request):
    basics = servise.get_basic()
    ctx = {
        "basics": basics,
    }
    return render(request, 'dashboard/basic/list.html', ctx)


def basic_create(request):
    model = Basic_menu()
    form = Basic_menuForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('basic_list')
        else:
            return print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/basic/form.html', ctx)


def basic_edit(request, pk):
    model = Basic_menu.objects.get(id=pk)
    form = Basic_menuForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('basic_list')
        else:
            print(form.errors)
    ctx = {
        "form":form
    }
    return render(request, 'dashboard/basic/form.html', ctx)


def basic_delete(request, pk):
    model = Basic_menu.objects.get(id=pk)
    model.delete()
    return redirect('basic_list')


def category_list(request):
    categories = servise.get_category()
    ctx = {
        "categories": categories,
    }
    return render(request, 'dashboard/category/list.html', ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_edit(request, pk):
    model = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_delete(request, pk):
    model = Category.objects.get(id=pk)
    model.delete()
    return redirect('category_list')


def news_list(request):
    news = servise.get_news()
    ctx = {
        "news": news,
    }
    return render(request, 'dashboard/news/list.html', ctx)


def news_create(request):
    model = News()
    form = NewsForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_edit(request, pk):
    model = News.objects.get(id=pk)
    form = NewsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news-list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_delete(request, pk):
    model = News.objects.get(id=pk)
    model.delete()
    return redirect('news_list')


def teacher_list(request):
    teachers = servise.get_teacher()
    ctx = {
        "teachers": teachers,
    }
    return render(request, 'dashboard/teacher/list.html', ctx)


def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/teacher/form.html', ctx)


def teacher_edit(request, pk):
    model = Teacher.objects.get(id=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/teacher/form.html', ctx)


def teacher_delete(request, pk):
    model = Teacher.objects.get(id=pk)
    model.delete()
    return redirect('teacher_list')
