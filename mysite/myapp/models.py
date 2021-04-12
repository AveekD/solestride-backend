from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class User(models.Model):
    objects =  UserManager()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='user')
    password = models.CharField(max_length=100, default='password')
    sex =  models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    