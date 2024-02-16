from django.contrib import admin

# Register your models here.
from django.contrib import admin
from german_collection.models import manufacturer,car_model,segment
# Register your models here.
admin.site.register(manufacturer)
admin.site.register(car_model)
admin.site.register(segment)