from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Seasons
from rest_framework.exceptions import NotFound

from .serializers.common import SeasonsSerializer
from .serializers.populated import PopulatedSeasonSerializer

class SeasonDateLocationsView(APIView):
    def get(self, request):
        seasons_queryset = Seasons.objects.all()
        seralized_season = SeasonsSerializer(seasons_queryset, many=True)
        return Response(seralized_season.data)


class SeasonalLocationsView(APIView):
    def get_object(self, season_id):
        try:
            season = Seasons.objects.get(id=season_id)
            return season
        except Seasons.DoesNotExist as err:
            print(err)
            raise NotFound("Season not found")
    
    def get (self, request, season_id):
        season = self.get_object(season_id)
        serialized_season = PopulatedSeasonSerializer(season)
        return Response(serialized_season.data)
