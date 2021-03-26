# myapi/urls.py
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
#from rest_framework.authtoken import views as authviews

urlpatterns = [
    url(r'api/user/', views.create_user),
    url(r'api/users/:field_id', views.get_field),
    url(r'api/login/', views.generate_token),
    #url(r'api-token-auth/', authviews.obtain_auth_token)
]