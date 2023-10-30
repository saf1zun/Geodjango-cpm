from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
# router.register('recipeCategorys', views.RecipeCategoryViewSet)
# router.register('ingredients', views.IngredientViewSet)
router.register('api', views.IncidentViewSet)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]