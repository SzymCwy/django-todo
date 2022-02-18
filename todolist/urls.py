"""todoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from todos.views import logout_view ,todo_update_view, todo_delete_view, user_view, home_view, login_view, registration_view, todos_list_view, todos_detail_view, todos_create_view
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('todos/list/', todos_list_view, name='list'),
    path('todos/list/<int:myid>/', todos_detail_view, name='detail'),
    path('todos/create', todos_create_view, name='create'),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('profile/', user_view, name = 'profile'),
    path('todos/list/<int:myid>/delete/', todo_delete_view, name = 'delete'),
    path('todos/list/<int:myid>/update/', todo_update_view, name = 'update'),


]
