from rest_framework.serializers import ModelSerializer
from ..models import Itinerary

class ItinerarySerializer(ModelSerializer):
    class Meta:
        model = Itinerary
        fields = '__all__'