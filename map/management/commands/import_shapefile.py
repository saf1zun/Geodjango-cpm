from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource
from map.models import PointOfInterest  # Import your model

class Command(BaseCommand):
    help = 'Import shapefile data into the database'

    def add_arguments(self, parser):
        parser.add_argument('shapefile', type=str, help='Path to the shapefile to import')

    def handle(self, *args, **options):
        shapefile_path = options['shapefile']

        # Open the shapefile using GDAL DataSource
        data_source = DataSource(shapefile_path)

        for layer in data_source:
            for feature in layer:
                geometry = feature.geom  # Get the geometry from the shapefile
                # You might need to convert the geometry to the correct SRID if necessary

                # Create a new instance of your model and populate it with data
                your_model_instance = PointOfInterest(
                    geometry_field=geometry,  # Replace with the actual field name
                    attribute_field=feature.get('attribute_field_name'),  # Replace with your attribute fields
                )

                your_model_instance.save()

        self.stdout.write(self.style.SUCCESS(f'Shapefile data imported successfully.'))
