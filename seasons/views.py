from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Seasons
from locations.models import Location
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers.common import SeasonsSerializer
from .serializers.populated import PopulatedSeasonSerializer
from locations.serializers.populated import PopulatedLocationSerializer

class SeasonDateLocationsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        start_month = request.query_params.get("start_month")
        end_month = request.query_params.get("end_month")

        if not start_month or not end_month:
            matching_seasons = Seasons.objects.all()
        else:

            # return Response({ "message": "Please provide start_month and end_month" })

            valid_months = Seasons.get_valid_months()
            if start_month not in valid_months or end_month not in valid_months:
                return Response({ "message": "Invalid month values provided" })

            matching_seasons = Seasons.objects.filter(start_month__lte=end_month, end_month__gte=start_month)

        if not matching_seasons.exists():
            return Response({ "message": "No matching seasons found" })

        locations = Location.objects.filter(seasons__in=matching_seasons).distinct()

        if not locations.exists():
            return Response({ "message": "No locations found for these seasons" })

        serialized_locations = PopulatedLocationSerializer(locations, many=True).data
        serialized_seasons = SeasonsSerializer(matching_seasons, many=True).data

        return Response({
            "locations": serialized_locations,
            "seasons": serialized_seasons
        })


class SeasonalLocationsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
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
