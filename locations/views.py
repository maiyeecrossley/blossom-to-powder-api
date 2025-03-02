from rest_framework.views import APIView
from rest_framework.reponse import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Location

from users.permissions import IsOwnerOrAdmin
from .serializers.common import LocationSerializer

class LocationListView(APIView):

    def get(self, request):
        locations_queryset = Location.objects.all()
        serialized_location = LocationSerializer(locations_queryset, many=True)
        return Response(serialized_location.data, 200)


#     def post(self, request):
#         serialized_location = LocationSerializer(data=request.data)

#         if serialized_location.is_valid():
#             serialized_location.save()
#             return Response(serialized_location.data, 201)
        
#         return Response(serialized_location.errors, 422)


# class LocationItineraryDetailView(APIView):
#     permission_classes = [IsAdmin]

#     def get_object(self, request, location_id):
#         try:
#             location = Location.objects.get(id=location_id)
#             return location
#         except Location.DoesNotExist as err:
#             print(err)
#             raise NotFound("Location not found")


#     def delete(self, request, location_id):
#         location_itinerary = self.get_object(location_id)
#         location_itinerary.delete() 
