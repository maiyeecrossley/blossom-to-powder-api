from .common import ItinerarySerializer
from locations.serializers.common import LocationSerializer

class PopulatedItinerarySerializer(ItinerarySerializer):
    locations = LocationSerializer(many=True)
