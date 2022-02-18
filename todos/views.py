import django.contrib.auth
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import todo, register
from .forms import TodosForm, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import *


# Create your views here.


def todos_list_view(request):
    queryset = todo.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'todo_list.html', context)


def todos_detail_view(request, myid):
    obj = get_object_or_404(todo, id=myid)
    context = {
        'object': obj
    }
    return render(request, 'todo_detail.html', context)


def todos_create_view(request):
    form = TodosForm(request.POST or None)
    if form.is_valid():
        todoobj = form.save(commit=False)
        todoobj.author = request.user
        todoobj.save()
        form = TodosForm()
    context = {
        'form': form
    }
    return render(request, 'todo_create.html', context)


def registration_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()

        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        user.save()
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    form = LoginForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        username = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect('profile')
        else:
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def home_view(request):
    return render(request, 'home.html', {})


def user_view(request):
    if request.user.is_authenticated:

        queryset = todo.objects.filter(author=request.user)
        context = {
            'objects': queryset
        }
        return render(request, 'user.html', context)
    else:
        return redirect('../../')


def todo_delete_view(request, myid):
    if request.user.is_authenticated:
        obj = get_object_or_404(todo, id=myid)
        if request.user == getattr(obj, 'author'):
            if request.method == 'POST':
                obj.delete()
                return redirect('/profile/')
            context = {
                'object': obj
            }
            return render(request,'delete.html', context)
        else:
            return redirect('login')


def todo_update_view(request, myid):
    if request.user.is_authenticated:
        obj = get_object_or_404(todo, id=myid)
        if request.user == getattr(obj, 'author'):
            form = TodosForm(instance=obj)
            if request.method == "POST":
                if form.is_valid():
                    form.save()
                    return redirect('../')
            context = {
                'form': form
            }
            return render(request, 'update.html', context)
        else:
            return redirect('login')


def logout_view(request):
    django.contrib.auth.logout(request)

    return render(request, 'logout.html', {})
