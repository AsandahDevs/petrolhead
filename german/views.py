from django.http import HttpRequest, HttpResponse
from rest_framework import response
from rest_framework import status
from rest_framework.decorators import APIView
from german.models import manufacturer,car_model,segment
from serializers import german_serializer

@APIView(['GET'])
def manufacturers(request:HttpRequest):
    #gets list of manufacturers
    try:
        car_manufacturers = manufacturer.objects.all()
    except DoesNotExist:
        pass
    serializer = german_serializer(car_manufacturers)
    return response(serializer.data,status=status.HTTP_200_OK)

@APIView(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're viewing the german_cars index.")
