from django.http import Http404, HttpRequest
from rest_framework import response
from rest_framework import status
from rest_framework.views import APIView
from german_collection.models import Manufacturer,CarModel,Segment
from .serializer import CarModelSerializer, ManufacturerSerializer

class manufacturers(APIView):
    def get(self,request:HttpRequest):
        #gets list of manufacturers
        try:
            car_manufacturers = Manufacturer.objects.all()
        except Manufacturer.DoesNotExist:
            raise Http404('No Manufacturer(s) were found')
        serializer = ManufacturerSerializer(car_manufacturers,many=True)
        return response.Response(serializer.data,status=status.HTTP_200_OK)

class add_car_manufacturer(APIView):
    def post(self,request:HttpRequest):
        # adds a new car Manufacturer to the database
        new_car_manufacturer=ManufacturerSerializer(data=request.data)
        if new_car_manufacturer.is_valid():
            new_car_manufacturer.save()
            return response.Response(new_car_manufacturer.data,status=status.HTTP_201_CREATED)
        return response.Response(new_car_manufacturer.errors,status=status.HTTP_400_BAD_REQUEST)

class update_car_manufacturer_details(APIView):
    def put(self,request:HttpRequest,id):
        # updates existing car Manufacturer details
        car_manufacturer = Manufacturer.objects.get(pk=id)
        serializer = ManufacturerSerializer(car_manufacturer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class delete_manfacturer(APIView):
    def delete(self,request,id):
        # deletes a manfacturer
          car_manufacturer = Manufacturer.objects.get(pk=id)
          car_manufacturer.delete()
          return response.Response(status=status.HTTP_204_NO_CONTENT)

class manufacturer_models(APIView):
    def get(self, request:HttpRequest):
        try:
         models = CarModel.objects.all()
        except CarModel.DoesNotExist:
         raise Http404('No Model(s) were found')
        serializer = CarModelSerializer(models,many=True)
        return response.Response(serializer.data,status=status.HTTP_200_OK)
    
class add_model(APIView):
    def post(self,request:HttpRequest):
        model = CarModelSerializer(data=request.data)
        print(model)
        if model.is_valid():
            model.save()
            return response.Response(model.data,status=status.HTTP_201_CREATED)
        return response.Response(model.data,status=status.HTTP_400_BAD_REQUEST)