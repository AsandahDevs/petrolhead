from django.contrib import admin
from german.models import manufacturer,car_model,segment
# Register your models here.
admin.site.register(manufacturer,car_model,segment)