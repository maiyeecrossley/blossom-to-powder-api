from .common import LocationSerializer
from seasons.serializers.common import SeasonsSerializer

class PopulatedLocationSerializer(LocationSerializer):
    seasons = SeasonsSerializer(many = True)
