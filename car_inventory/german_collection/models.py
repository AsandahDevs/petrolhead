from django.db import models

# Create your models here.
from django.db import models

class manufacturer(models.Model):
    brand = models.CharField(primary_key=True,max_length=20)
    founder = models.TextField()
    year_founded = models.IntegerField()
    headquarters = models.TextField()

    def __str__(self) -> str:
        return f'{self.brand} {self.founder} {self.year_founded} {self.headquarters}'

class car_model(models.Model):
    model_name = models.CharField(max_length=20)
    model_year = models.IntegerField()
    price = models.ImageField()
    transmission_type = models.TextField()
    engine_position = models.TextField(blank=True)
    engine_litre = models.CharField(max_length=5)
    fuel_consumption = models.CharField(max_length=10)
    fuel_type = models.TextField()
    cylinder_layout = models.CharField(max_length=10)
    horsepower = models.IntegerField()
    torque = models.IntegerField()
    top_speed = models.IntegerField()
    image_url = models.URLField()
    manufacturer = models.ForeignKey(manufacturer,on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f'{self.model_name} {self.model_year} {self.price} {self.transmission_type} {self.engine_position} {self.engine_litre} {self.fuel_consumption} {self.fuel_type} {self.cylinder_layout} {self.horsepower} {self.torque} {self.top_speed} {self.image_url} {self.manufacturer}'

class segment(models.Model):
    segment = models.TextField()
    car_model = models.ForeignKey(car_model,on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.segment