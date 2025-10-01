from rest_framework import serializers
from .models import FlightRequest, Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class FlightRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightRequest
        fields = '__all__'
