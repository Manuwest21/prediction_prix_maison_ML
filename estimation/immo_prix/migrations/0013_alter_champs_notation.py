# Generated by Django 4.1.7 on 2023-03-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immo_prix', '0012_alter_champs_salle_de_bain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champs',
            name='notation',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13')]),
        ),
    ]