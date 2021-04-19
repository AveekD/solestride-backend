from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class Person(models.Model):
    # objects =  UserManager()
    firstName = models.CharField(max_length=100, default='undefined')
    lastName = models.CharField(max_length=100, default='undefined')
    email = models.CharField(max_length=100, default='undefined')
    username = models.CharField(max_length=100, default='user')
    password = models.CharField(max_length=100, default='password')
    sex =  models.CharField(max_length=100, default='undefined')
    height = models.CharField(max_length=100, default='undefined')
    weight = models.CharField(max_length=100, default='undefined')
    