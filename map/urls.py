from django.urls import path
from .views import HomeView
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search_results/', views.search_results, name='search_results'),
    path('facility_detail/<int:pk>/', views.facility_detail, name='facility_detail'),
    path('map_results/', views.map_results, name='map_results'),
    # Add other URL patterns as needed

]
