# urls.py (inside your app, e.g., "map")

# spatialq/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('point-in-polygon/', views.point_in_polygon, name='point_in_polygon'),
    # path('nearest-facility/', views.nearest_facility, name='nearest_facility'),
    # path('population-density/', views.population_density, name='population_density'),
    # path('zone-woreda/', views.zone_woreda, name='zone_woreda'),
    # Define more URL patterns for other spatial queries
    path('health-facilities-in-region/', views.health_facilities_in_region, name='health_facilities_in_region'),
    # Other URL patterns]
]