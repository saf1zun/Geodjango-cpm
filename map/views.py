from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse
import random
import folium
from folium import GeoJson, FeatureGroup
from .models import EthioHealthFacilities, EthiopianRegions, Woreda, Population
from django.db.models import Q
from django.http import JsonResponse

from .serializers import EthioHealthFacilitiesSerializer

def random_color(feature):
    colors = ['#FF5733', '#FFC300', '#33FF33', '#33FFFC', '#CF33F7', '#6333FF']
    return {'fillColor': random.choice(colors), 'color': random.choice(colors)}



def graded_color(population_value):
    if population_value < 100000:
        return {'fillColor': 'green', 'fillOpacity': 0.7, 'color': 'green'}
    elif 100000 <= population_value < 500000:
        return {'fillColor': 'yellow', 'fillOpacity': 0.7, 'color': 'yellow'}
    elif 500000 <= population_value < 1000000:
        return {'fillColor': 'orange', 'fillOpacity': 0.7, 'color': 'orange'}
    else:
        return {'fillColor': 'red', 'fillOpacity': 0.7, 'color': 'red'}


class HomeView(TemplateView):
    template_name = 'map/map.html'

    def get_context_data(self, **kwargs):
        # Create the base map
        m = folium.Map(location=[9.0236, 38.9062], zoom_start=6)

        # Add Ethiopian Regions
        ethiopian_regions = EthiopianRegions.objects.all()
        Ethiopian_Regions_fg = FeatureGroup(name='Ethiopian_Regions')

        for region in ethiopian_regions:
            popup_content = f"Region Name: {region.regionname}"
            style = random_color(region)
            GeoJson(region.geom.geojson, style_function=lambda x: style, tooltip=popup_content).add_to(Ethiopian_Regions_fg)

        Ethiopian_Regions_fg.add_to(m)

        # Add Woreda data
        woredas = Woreda.objects.all()
        Woreda_fg = FeatureGroup(name='Woredas')

        for woreda in woredas:
            popup_content = f"Woreda Name: {woreda.w_name}"
            style = random_color(woreda)
            GeoJson(woreda.geom.geojson, style_function=lambda x: style, tooltip=popup_content).add_to(Woreda_fg)

        Woreda_fg.add_to(m)

        # Add Population data
        population_data = Population.objects.all()
        Population_fg = FeatureGroup(name='Population')

        for entry in population_data:
            popup_content = f"Area: {entry.area}<br>Population: {entry.popest94}"
            style = graded_color(entry.popest94)
            GeoJson(entry.geom.geojson, style_function=lambda x: style, tooltip=popup_content).add_to(Population_fg)

        Population_fg.add_to(m)

        # Add Ethio Health Facilities
        ethio_health_facilities = EthioHealthFacilities.objects.all()
        Ethio_Health_Facilities_fg = FeatureGroup(name='Ethio_Health_Facilities')

        facility_categories = set(ethio_health_facilities.values_list('facility_t', flat=True))
        for category in facility_categories:
            category_fg = FeatureGroup(name=category)
            for facility in ethio_health_facilities.filter(facility_t=category):
                popup_content = f"Facility Type: {facility.facility_t}<br>Facility Name: {facility.facility_n}"
                style = random_color(facility)
                folium.CircleMarker(location=[float(facility.lat), float(facility.long)], radius=2, fill=True, color=style['color'], fill_opacity=1, popup=popup_content).add_to(category_fg)
            category_fg.add_to(m)

        # Add Layer Control to toggle layers
        folium.LayerControl(collapsed=False).add_to(m)

        # Convert the map to HTML
        m_html = m._repr_html_()

        # Add context data for rendering in the template
        context = {
            'my_map': m_html,
        }
        return context




def search_results(request):
    query = request.GET.get('query')

    if query:
        results = EthioHealthFacilities.objects.filter(
            Q(facility_n__icontains=query)
        )
    else:
        # If no query is provided, can handle this case
        results = []

    return render(request, 'map/search.html', {'results': results})


def filter_facilities(request):
    ownership = request.GET.get('ownership')
    region = request.GET.get('region')

    facilities = EthioHealthFacilities.objects.all()

    if ownership:
        facilities = facilities.filter(ownership=ownership)

    if region:
        facilities = facilities.filter(region__regionname=region)

    return render(request, 'map/filtered_facilities.html', {'facilities': facilities})



def facility_detail(request, pk):
    facility = get_object_or_404(EthioHealthFacilities, pk=pk)
    return render(request, 'map/facility_detail.html', {'facility': facility})







def map_results(request):
    query = request.GET.get('query')  # Retrieve the search query from the URL

    center_lat, center_long = 9.1450, 40.489673  # Default center

    if query:
        # Perform a search based on the query
        results = EthioHealthFacilities.objects.filter(
            facility_n__icontains=query
        )

        if results:
            # Get the coordinates of the first search result
            first_result = results.first()
            center_lat = float(first_result.lat)
            center_long = float(first_result.long)

        # Create a Folium map centered at the specific location
        m = folium.Map(location=[center_lat, center_long], zoom_start=10)

        # Add markers for search results
        for result in results:
            lat = float(result.lat)
            long = float(result.long)
            facility_name = result.facility_n

            # Create a marker and add it to the map
            folium.Marker([lat, long], popup=facility_name).add_to(m)

        # Convert the map to HTML
        map_html = m._repr_html_()

    else:
        # Handle the case where no query is provided
        map_html = ""

    return render(request, 'map/map_results.html', {'map_html': map_html})





