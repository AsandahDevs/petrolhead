# Create your models here.
from django.db import models

class Manufacturer(models.Model):
    brand = models.CharField(max_length=20, blank=False)
    founder = models.TextField(blank=False)
    year_founded = models.IntegerField()
    headquarters = models.TextField()

    def __str__(self) -> str:
        return f'{self.brand} {self.founder} {self.year_founded} {self.headquarters}'

class CarModel(models.Model):
    manufacturer_id = models.ForeignKey(Manufacturer,on_delete=models.RESTRICT,related_name='car_models')
    model_name = models.CharField(max_length=20)
    model_year = models.IntegerField()
    price = models.IntegerField()
    transmission_type = models.TextField()
    engine_position = models.TextField(blank=False,default='Front')
    engine_litre = models.CharField(max_length=5)
    fuel_consumption = models.CharField(max_length=10)
    fuel_type = models.TextField(default='petrol')
    cylinder_layout = models.CharField(max_length=10)
    horsepower = models.IntegerField()
    torque = models.IntegerField()
    top_speed = models.IntegerField()
    image_url = models.URLField()

    def __str__(self) -> str:
        return f'{self.manufacturer_id} {self.model_name} {self.model_year} {self.price} {self.transmission_type} {self.engine_position} {self.engine_litre} {self.fuel_consumption} {self.fuel_type} {self.cylinder_layout} {self.horsepower} {self.torque} {self.top_speed} {self.image_url}'

class Segment(models.Model):
    car_model_id = models.ForeignKey(CarModel,on_delete=models.RESTRICT,related_name='segments')
    segment = models.TextField()

    def __str__(self) -> str:
        return self.segment