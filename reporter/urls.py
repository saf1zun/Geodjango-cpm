from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register('maps', views.IncidentViewSet)


app_name = 'reporter'

urlpatterns = [
    path('', include(router.urls))
]