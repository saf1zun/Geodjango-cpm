# Generated by Django 4.2.6 on 2023-10-29 00:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EthioHealthFacilities',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(blank=True, max_length=254, null=True)),
                ('admin1', models.CharField(blank=True, max_length=254, null=True)),
                ('facility_n', models.CharField(blank=True, max_length=254, null=True)),
                ('facility_t', models.CharField(blank=True, max_length=254, null=True)),
                ('ownership', models.CharField(blank=True, max_length=254, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('long', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('ll_source', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'ethio_health_facilities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EthiopianRegions',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('regionname', models.CharField(blank=True, max_length=254, null=True)),
                ('confirmed_field', models.IntegerField(blank=True, db_column='confirmed_', null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'ethiopian_regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.FloatField(blank=True, null=True)),
                ('perimeter', models.FloatField(blank=True, null=True)),
                ('pop_id', models.FloatField(blank=True, null=True)),
                ('name1', models.CharField(blank=True, max_length=20, null=True)),
                ('name2', models.CharField(blank=True, max_length=20, null=True)),
                ('popest94', models.IntegerField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=5, null=True)),
                ('pop_1984', models.FloatField(blank=True, null=True)),
                ('pdens_1984', models.FloatField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'population',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Woreda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('W6ID', models.IntegerField()),
                ('W_NAME', models.CharField(max_length=255)),
                ('Z4ID', models.IntegerField()),
                ('REGION_R2I', models.CharField(max_length=255)),
                ('Pop_Den', models.FloatField()),
                ('Pop', models.IntegerField()),
                ('Region', models.CharField(max_length=255)),
                ('New_Code', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'Woreda',
                'verbose_name_plural': 'Woredas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('zon_name', models.CharField(blank=True, max_length=30, null=True)),
                ('first_regi', models.CharField(blank=True, max_length=20, null=True)),
                ('first_re_1', models.CharField(blank=True, max_length=2, null=True)),
                ('first_z4id', models.CharField(blank=True, max_length=6, null=True)),
                ('sum_area_k', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('sum_pop', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('confirmed_field', models.IntegerField(blank=True, db_column='confirmed_', null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'zones',
                'managed': False,
            },
        ),
    ]
