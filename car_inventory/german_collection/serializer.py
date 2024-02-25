from rest_framework import serializers
from german_collection.models import Manufacturer,CarModel,Segment
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
class ManufacturerSerializer(serializers.ModelSerializer):
    car_models = CarModelSerializer(many=True,read_only=True)
    class Meta:
        model = Manufacturer
        fields = '__all__'