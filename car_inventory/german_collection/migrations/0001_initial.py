# Generated by Django 5.0.2 on 2024-02-24 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='manufacturer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(default='', editable=False, max_length=20)),
                ('founder', models.TextField()),
                ('year_founded', models.IntegerField()),
                ('headquarters', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='car_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('model_year', models.IntegerField()),
                ('price', models.ImageField(upload_to='')),
                ('transmission_type', models.TextField()),
                ('engine_position', models.TextField(blank=True)),
                ('engine_litre', models.CharField(max_length=5)),
                ('fuel_consumption', models.CharField(max_length=10)),
                ('fuel_type', models.TextField()),
                ('cylinder_layout', models.CharField(max_length=10)),
                ('horsepower', models.IntegerField()),
                ('torque', models.IntegerField()),
                ('top_speed', models.IntegerField()),
                ('image_url', models.URLField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='german_collection.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment', models.TextField()),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='german_collection.car_model')),
            ],
        ),
    ]
