from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from myapp.models import User
from myapp.serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST', 'GET'])
def create_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            instance, created = User.objects.update_or_create(email=serializer.validated_data.get('email', None), defaults=serializer.validated_data)
            if not created:
                serializer.update(instance, serializer.validated_data)
            return response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
