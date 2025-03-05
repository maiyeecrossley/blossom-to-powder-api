from .common import ItinerarySerializer, ItineraryLocationSerializer
from locations.serializers.common import LocationSerializer

class PopulatedItineraryLocationSerializer(ItineraryLocationSerializer):
    location = LocationSerializer(read_only=True)
class PopulatedItinerarySerializer(ItinerarySerializer):
    locations = ItineraryLocationSerializer(source="itinerarylocation_set", many=True)
