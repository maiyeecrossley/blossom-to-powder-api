from rest_framework.serializers import ModelSerializer
from ..models import Seasons

class SeasonsSerializer(ModelSerializer):
    class Meta:
        model = Seasons
        fields = '__all__'