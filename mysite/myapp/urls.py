# myapi/urls.py
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    url(r'api/user/', views.create_user),
]