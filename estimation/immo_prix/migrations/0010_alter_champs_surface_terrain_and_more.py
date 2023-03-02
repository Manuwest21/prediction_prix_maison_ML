# Generated by Django 4.1.5 on 2023-03-02 04:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immo_prix', '0009_alter_champs_estimation_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champs',
            name='surface_terrain',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(-2)]),
        ),
        migrations.AlterField(
            model_name='champs',
            name='surface_terrain_15',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(-2)]),
        ),
    ]
