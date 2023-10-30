# map/models.py
from django.contrib.gis.db import models


class EthioHealthFacilities(models.Model):
    gid = models.AutoField(primary_key=True)
    country = models.CharField(max_length=254, blank=True, null=True)
    admin1 = models.CharField(max_length=254, blank=True, null=True)
    facility_n = models.CharField(max_length=254, blank=True, null=True)
    facility_t = models.CharField(max_length=254, blank=True, null=True)
    ownership = models.CharField(max_length=254, blank=True, null=True)
    lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    long = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ll_source = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ethio_health_facilities'









class EthiopianRegions(models.Model):
    gid = models.AutoField(primary_key=True)
    regionname = models.CharField(max_length=254, blank=True, null=True)
    confirmed_field = models.IntegerField(db_column='confirmed_', blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ethiopian_regions'
        

class Population(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    pop_id = models.FloatField(blank=True, null=True)
    name1 = models.CharField(max_length=20, blank=True, null=True)
    name2 = models.CharField(max_length=20, blank=True, null=True)
    popest94 = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=5, blank=True, null=True)
    pop_1984 = models.FloatField(blank=True, null=True)
    pdens_1984 = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'population'



class Zones(models.Model):
    gid = models.AutoField(primary_key=True)
    zon_name = models.CharField(max_length=30, blank=True, null=True)
    first_regi = models.CharField(max_length=20, blank=True, null=True)
    first_re_1 = models.CharField(max_length=2, blank=True, null=True)
    first_z4id = models.CharField(max_length=6, blank=True, null=True)
    sum_area_k = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sum_pop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    confirmed_field = models.IntegerField(db_column='confirmed_', blank=True, null=True)  # Field renamed because it ended with '_'
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zones'

    def __str__(self):
        return self.zon_name  # Display the zon_name in the admin site

class Woreda(models.Model):
    gid = models.AutoField(primary_key=True)
    w6id = models.CharField(max_length=6, blank=True, null=True)
    w_name = models.CharField(max_length=50, blank=True, null=True)
    z4id = models.CharField(max_length=6, blank=True, null=True)
    region_r2i = models.CharField(max_length=2, blank=True, null=True)
    pop_den = models.IntegerField(blank=True, null=True)
    pop = models.IntegerField(blank=True, null=True)
    zon_name = models.CharField(max_length=30, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    new_code = models.CharField(max_length=6, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'woreda'