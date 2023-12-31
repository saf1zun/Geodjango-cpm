# Generated by Django 4.2.6 on 2023-10-25 20:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Incidences',
                'db_table': 'Incidences',
            },
        ),
        migrations.CreateModel(
            name='Woredas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woredas', models.CharField(max_length=25)),
                ('codes', models.IntegerField()),
                ('cty_code', models.CharField(max_length=24)),
                ('dis', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Woredas',
            },
        ),
    ]
