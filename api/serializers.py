from rest_framework import serializers

from reporter.models import IncidentSpot


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncidentSpot
        fields = (
            'id','title' , 'description' ,'picture', 'geom'
        )
        read_only_fields = ('id',)
        