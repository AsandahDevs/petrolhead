from django.contrib import admin
from django.urls import  path
from german_collection import views

app_name = 'german_collection'
urlpatterns = [
 path('admin/', admin.site.urls),
 path('manufacturers/',views.manufacturers,name="manufacturers")
]