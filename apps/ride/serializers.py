from rest_framework import serializers
from apps.ride.models import Ride, RideEvent

class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    ride_events = RideEventSerializer(many=True, read_only=True, source='events')

    class Meta:
        model = Ride
        fields = '__all__'