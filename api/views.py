from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

from api import serializers
from reporter.models import IncidentSpot


# Create your views here.
class IncidentViewSet(viewsets.ModelViewSet):
    queryset = IncidentSpot.objects.all()
    serializer_class = serializers.IncidentSerializer
