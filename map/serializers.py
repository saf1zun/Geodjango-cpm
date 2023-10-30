from rest_framework import serializers
from .models import EthioHealthFacilities

class EthioHealthFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthioHealthFacilities
        fields = '__all__'