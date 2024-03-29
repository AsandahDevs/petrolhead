from django.contrib import admin
from django.urls import  path
from german_collection.views import add_car_manufacturer, add_model, car_model_by_manufacturer, delete_manfacturer, manufacturer_models, manufacturers, update_car_manufacturer_details

app_name = 'german_collection'
urlpatterns = [
 path('admin/', admin.site.urls),
 path('manufacturers',manufacturers.as_view(),name="manufacturers"),
 path('add-manufacturer', add_car_manufacturer.as_view(), name="add-manufacturer"),
 path('manufacturer/<int:id>', update_car_manufacturer_details.as_view(), name="update-manufacturer"),
 path('delete-manufacturer/<int:id>', delete_manfacturer.as_view(), name="delete-manufacturer"),
 path('manufacturer-models', manufacturer_models.as_view(),name="manufacturer-models"),
 path('manufacturer-models/<int:id>', car_model_by_manufacturer.as_view(),name="car-model-by-manufacturer"),
 path('model',add_model.as_view(),name="model")
]