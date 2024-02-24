from django.contrib import admin
from django.urls import  path
from german_collection import views

app_name = 'german_collection'
urlpatterns = [
 path('admin/', admin.site.urls),
 path('manufacturers',views.manufacturers,name="manufacturers"),
 path('add-manufacturer', views.add_car_manufacturer, name="add-manufacturer"),
 path('manufacturer/<int:id>', views.update_car_manufacturer_details, name="update-manufacturer")
]