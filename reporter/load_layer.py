import os
from django.contrib.gis.utils import LayerMapping
from .models import Woredas

woreda_mapping = {
    'woredas' : 'W_NAME',
    'population' : 'Pop',
    'Zone' : 'ZON_NAME',
    'geom' : 'MULTIPOLYGON',
}

woreda_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/wored.shp'))

def run(verbose=True):
	lm = LayerMapping(Woredas, woreda_shp, woreda_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)