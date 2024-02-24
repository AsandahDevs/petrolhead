from django.http import Http404, HttpRequest
from rest_framework import response
from rest_framework import status
from rest_framework.views import APIView
from german_collection.models import manufacturer,car_model,segment
from .serializer import german_serializer

class manufacturers(APIView):
    def get(self,request:HttpRequest):
        #gets list of manufacturers
        try:
            car_manufacturers = manufacturer.objects.all()
        except manufacturer.DoesNotExist:
            raise Http404('No manufacturer(s) were found')
        serializer = german_serializer(car_manufacturers,many=True)
        return response.Response(serializer.data,status=status.HTTP_200_OK)

class add_car_manufacturer(APIView):
    def post(self,request:HttpRequest):
        # adds a new car manufacturer to the database
        new_car_manufacturer=german_serializer(data=request.data)
        if new_car_manufacturer.is_valid():
            new_car_manufacturer.save()
            return response.Response(new_car_manufacturer.data,status=status.HTTP_201_CREATED)
        return response.Response(new_car_manufacturer.errors,status=status.HTTP_400_BAD_REQUEST)

class update_car_manufacturer_details(APIView):
    def put(self,request:HttpRequest,id):
        # updates existing car manufacturer details
        car_manufacturer = manufacturer.objects.get(pk=id)
        serializer = german_serializer(car_manufacturer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
