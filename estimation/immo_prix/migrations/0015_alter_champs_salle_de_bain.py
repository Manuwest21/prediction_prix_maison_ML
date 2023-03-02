# Generated by Django 4.1.7 on 2023-03-02 13:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immo_prix', '0014_alter_champs_notation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champs',
            name='salle_de_bain',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(0)]),
        ),
    ]
