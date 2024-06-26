# Generated by Django 5.0.6 on 2024-06-07 15:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GrowthStages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('growth_level', models.SmallIntegerField(verbose_name='Nivel de crescimento')),
            ],
        ),
        migrations.CreateModel(
            name='PlanttingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('min_temperature', models.SmallIntegerField(verbose_name='Temperatura minima')),
                ('max_temperature', models.SmallIntegerField(verbose_name='Temperatura maxima')),
                ('min_umidty', models.SmallIntegerField(verbose_name='Umidade minima')),
                ('max_umidty', models.SmallIntegerField(verbose_name='Umidade maxima')),
                ('growth_stages', models.ManyToManyField(to='plants.growthstages', verbose_name='Estados de crescimento')),
            ],
        ),
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(verbose_name='Ativo')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Dono')),
                ('plant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.plant', verbose_name='Planta')),
            ],
        ),
    ]
