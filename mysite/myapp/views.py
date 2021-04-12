from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from myapp.models import User
from myapp.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

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
        user = User.objects.create_user(request.headers["username"], request.headers["email"], request.headers["password"])
        user.save()
        # user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(request.headers["username"], request.headers["email"], request.headers["password"], 
        request.headers["first_name"], request.headers["last_name"], request.headers["sex"], request.headers["height"], request.headers["weight"])
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
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    print(username)
    print(password)
    user = authenticate(username = username, password = password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


# ## get all unread notifications
# @api_view(['GET'])
# def get_all_unread_notficiations():

# ## delete a notficiation from the unread array
# @api_view(['DELETE'])
# def delete_read_notification():



