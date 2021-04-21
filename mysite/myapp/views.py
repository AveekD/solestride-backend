from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from myapp.models import Person
from django.contrib.auth.models import User
from myapp.serializers import PersonSerializer
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
        person = Person.objects.create(
            firstName = request.headers["firstName"],
            lastName = request.headers["lastName"],
            email = request.headers["email"], 
            username = request.headers["username"], 
            password = request.headers["password"],
            sex = request.headers["sex"],
            height = request.headers["height"],
            weight = request.headers["weight"],
        )
        person.save()
        user = User.objects.create_user(username = request.headers["username"], email = request.headers["email"], password = request.headers["password"])
        person_serializer = PersonSerializer(person)
        person_serializer_validate = PersonSerializer(data=person_serializer.data)
        if person_serializer_validate.is_valid():
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        serializer = PersonSerializer(user_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)

# generates token for user creation
@api_view(['GET'])
def generate_token(request):
    username = request.headers["username"]
    password = request.headers["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
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



