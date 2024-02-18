from rest_framework import serializers
from german_collection.models import manufacturer,car_model,segment

class german_serializer(serializers.ModelSerializer):
     class Meta:
        model = manufacturer
        fields = '__all__'