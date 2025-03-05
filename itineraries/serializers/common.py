from rest_framework.serializers import ModelSerializer, IntegerField
from ..models import Itinerary, Location, ItineraryLocation
from locations.serializers.common import LocationSerializer

class ItineraryLocationSerializer(ModelSerializer):
    location = LocationSerializer(read_only=True)
    class Meta:
        model = ItineraryLocation
        fields = ["location", "location_visit_date"]

class ItinerarySerializer(ModelSerializer):
    locations = ItineraryLocationSerializer(many=True, read_only=True)
    class Meta:
        model = Itinerary
        fields = ["id", "trip_name", "trip_start_date", "trip_end_date", "owner", "locations"]
        extra_kwargs = {"owner": {"read_only": True}}