from rest_framework.serializers import ModelSerializer, IntegerField
from ..models import Itinerary, Location, ItineraryLocation
from locations.serializers.common import LocationSerializer

class ItineraryLocationSerializer(ModelSerializer):

    location = LocationSerializer(read_only=True)
    location_id = IntegerField(write_only=True)
    class Meta:
        model = ItineraryLocation
        fields = ["id", "location", "location_id", "visit_date"]

class ItinerarySerializer(ModelSerializer):
    locations = ItineraryLocationSerializer(source="itinerarylocation_set", many=True, read_only=True)
    class Meta:
        model = Itinerary
        fields = ["id", "trip_name", "trip_start_date", "trip_end_date", "owner", "locations"]
        extra_kwargs = {"owner": {"read_only": True}}