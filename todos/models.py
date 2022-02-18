from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    till = models.DateTimeField()
    done = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class login(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    email = models.EmailField()