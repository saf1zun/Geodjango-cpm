from djgeojson.fields import GeometryCollectionField
from django.db import models

class IncidentSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = GeometryCollectionField()
    
    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url

# Create your models here.
