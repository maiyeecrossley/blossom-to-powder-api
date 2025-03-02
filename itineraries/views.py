from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Itinerary

from users.permissions import IsOwnerOrAdmin

from .serializers.common import ItinerarySerializer
from .serializers.populated import PopulatedItinerarySerializer

class ItineraryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        itinerary_queryset = Itinerary.objects.filter(owner=request.user)
        serialized_itinerary = ItinerarySerializer(itinerary_queryset, many=True)
        return Response(serialized_itinerary.data, 200)


    def post(self, request):
        serialized_itinerary = ItinerarySerializer(data=request.data)

        if serialized_itinerary.is_valid():
            serialized_itinerary.save()
            return Response(serialized_itinerary.data, 201)

        return Response(serialized_itinerary.errors, 422)    


class ItineraryDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self, request, itinerary_id):
        try:
            itinerary = Itinerary.objects.get(id=itinerary_id)
            self.check_object_permissions(request, itinerary)
            return itinerary
        except Itinerary.DoesNotExist as err:
            print(err)
            raise NotFound("Itinerary not found")


    def get(self, request, itinerary_id):
        itinerary = self.get_object(request, itinerary_id)
        serialized_itinerary = PopulatedItinerarySerializer(itinerary)
        return Response(serialized_itinerary.data, 200)

    
    def patch(self, request, itinerary_id):
        itinerary = self.get_object(request, itinerary_id)
        serialized_itinerary = ItinerarySerializer(itinerary, data=request.data)

        if serialized_itinerary.is_valid():
            serialized_itinerary.save()
            return Response(serialized_itinerary.data, 201)

        return Reponse(serialized_itinerary.errors, 422)


    def delete(self, request, itinerary_id):
        itinerary = self.get_object(request, itinerary_id)
        itinerary.delete()
        return Response(status=204)