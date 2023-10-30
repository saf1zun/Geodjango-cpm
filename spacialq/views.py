from django.http import JsonResponse
from django.contrib.gis.db.models import Q
from map.models import EthioHealthFacilities, EthiopianRegions

def health_facilities_in_region(request):
    # Example: Find health facilities within a specific region polygon
    region_name = "Somali"  # Replace with the actual region name
    region = EthiopianRegions.objects.get(regionname=region_name)
    facilities = EthioHealthFacilities.objects.filter(geom__within=region.geom)
    
    # Process the query results
    results = [{'facility_name': facility.facility_n} for facility in facilities]
    return JsonResponse({'results': results})
