# Generated by Django 4.1.5 on 2023-03-02 02:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immo_prix', '0004_alter_champs_code_postal'),
    ]

    operations = [
        migrations.AddField(
            model_name='formu',
            name='tit',
            field=models.CharField(default=300000, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='champs',
            name='code_postal',
            field=models.IntegerField(choices=[(98178, '98178'), (98125, '98125'), (98028, '98028'), (98136, '98136'), (98074, '98074'), (98053, '98053'), (98003, '98003'), (98198, '98198'), (98146, '98146'), (98038, '98038'), (98007, '98007'), (98115, '98115'), (98107, '98107'), (98126, '98126'), (98019, '98019'), (98103, '98103'), (98002, '98002'), (98133, '98133'), (98040, '98040'), (98092, '98092'), (98030, '98030'), (98119, '98119'), (98112, '98112'), (98052, '98052'), (98027, '98027'), (98117, '98117'), (98058, '98058'), (98001, '98001'), (98056, '98056'), (98166, '98166'), (98023, '98023'), (98070, '98070'), (98148, '98148'), (98105, '98105'), (98042, '98042'), (98008, '98008'), (98059, '98059'), (98122, '98122'), (98144, '98144'), (98004, '98004'), (98005, '98005'), (98034, '98034'), (98075, '98075'), (98116, '98116'), (98010, '98010'), (98118, '98118'), (98199, '98199'), (98032, '98032'), (98045, '98045'), (98102, '98102'), (98077, '98077'), (98108, '98108'), (98168, '98168'), (98177, '98177'), (98065, '98065'), (98029, '98029'), (98006, '98066'), (98109, '98109'), (98022, '98022'), (98033, '98033'), (98155, '98155'), (98024, '98024'), (98011, '98011'), (98031, '98031'), (98106, '98106'), (98072, '98072'), (98188, '98188'), (98014, '98014'), (98055, '98055'), (98039, '98039')]),
        ),
        migrations.AlterField(
            model_name='champs',
            name='salle_de_bain',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='champs',
            name='surface_habitable',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5000), django.core.validators.MinValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='champs',
            name='surface_terrain',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='champs',
            name='surface_terrain_15',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='champs',
            name='vue',
            field=models.IntegerField(choices=[(1, 'pas de vue particulière'), (2, 'vue passable'), (3, 'belle vue'), (4, 'trés belle vue')]),
        ),
        migrations.AlterField(
            model_name='champs',
            name='vue_sur_mer',
            field=models.IntegerField(choices=[(0, 'pas de vue sur mer'), (1, 'vue sur mer')]),
        ),
    ]
