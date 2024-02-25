from django.contrib import admin

# Register your models here.
from django.contrib import admin
from german_collection.models import Manufacturer,CarModel,Segment
# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(CarModel)
admin.site.register(Segment)