from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from myapp.models import User
from myapp.serializers import UserSerializer
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.

# creates and stores user with headers: username, password, email, sex, height, and weight
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# gets specific field (sex/height/weight)
@api_view(['GET'])
def get_field(request, field_id):
    if request.method == 'GET':
        user_instance = self.get_field(field_id, request.user_data.id)
        if not user_instance:
            return Response(
                {"res": "Object with field id does not exists"},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)

# generates token for user creation
@api_view(['GET'])
def generate_token(request):
    username = request.headers["username"]
    password = request.headers["password"]
    print(username)
    print(password)
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username, password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)