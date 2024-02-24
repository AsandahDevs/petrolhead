from django.contrib import admin
from django.urls import  path
from german_collection.views import add_car_manufacturer, manufacturers, update_car_manufacturer_details

app_name = 'german_collection'
urlpatterns = [
 path('admin/', admin.site.urls),
 path('manufacturers',manufacturers.as_view(),name="manufacturers"),
 path('add-manufacturer', add_car_manufacturer.as_view(), name="add-manufacturer"),
 path('manufacturer/<int:id>', update_car_manufacturer_details.as_view(), name="update-manufacturer")
]