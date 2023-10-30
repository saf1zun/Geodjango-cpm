from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as incident_model




admin.site.register(incident_model.IncidentSpot, LeafletGeoAdmin)