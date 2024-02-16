from rest_framework import serializers
from german_collection.models import manufacturer,car_model,segment

class german_serializer(serializers.ModelSerializer):
     class Meta:
        model = manufacturer
        fields = '__all__'

     class Meta:
        model = car_model
        fields = '__all__'

     class Meta:
        model = segment
        fields = '__all__'