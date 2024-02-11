from django.contrib import admin
from django.urls import  path
from german import views

urlpatterns = [
 path('admin/', admin.site.urls),
 path('manufacturers/',views.manufacturers(),name="manufacturers"),
 path("", views.index, name="index"),
]