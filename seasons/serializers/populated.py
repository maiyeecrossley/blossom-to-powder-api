from .common import SeasonsSerializer
from locations.serializers.common import LocationSerializer

class PopulatedSeasonSerializer(SeasonsSerializer):
    seasonal_locations = LocationSerializer(many = True)