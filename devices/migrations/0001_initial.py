# Generated by Django 5.0.6 on 2024-06-07 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StacVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('get_temperature', models.BooleanField(verbose_name='Coleta temperatura')),
                ('get_pressure', models.BooleanField(verbose_name='Coleta pressão')),
                ('get_vibration', models.BooleanField(verbose_name='Coleta vibração')),
                ('get_umidity', models.BooleanField(verbose_name='Coleta umidade')),
            ],
        ),
        migrations.CreateModel(
            name='Stac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(verbose_name='Ativo')),
                ('planting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.planting', verbose_name='Plantio')),
                ('version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.stacversion')),
            ],
        ),
        migrations.CreateModel(
            name='CollectedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('data', models.JSONField(verbose_name='Dados')),
                ('stac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.stac')),
            ],
        ),
    ]
