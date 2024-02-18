from django.http import Http404, HttpRequest
from rest_framework import response
from rest_framework import status
from rest_framework.decorators import api_view
from german_collection.models import manufacturer,car_model,segment
from .serializer import german_serializer

@api_view(['GET'])
def manufacturers(request:HttpRequest):
    #gets list of manufacturers
    try:
        car_manufacturers = manufacturer.objects.all()
    except manufacturer.DoesNotExist:
        raise Http404('No manufacturer(s) were found')
    serializer = german_serializer(car_manufacturers,many=True)
    return response.Response(serializer.data,status=status.HTTP_200_OK)
