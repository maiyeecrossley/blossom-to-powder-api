from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Itinerary, ItineraryLocation
from locations.models import Location

from users.permissions import IsOwnerOrAdmin

from .serializers.common import ItinerarySerializer, ItineraryLocationSerializer
from .serializers.populated import PopulatedItinerarySerializer


class ItineraryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        itinerary_queryset = Itinerary.objects.filter(owner=request.user)
        serialized_itinerary = PopulatedItinerarySerializer(itinerary_queryset, many=True)
        return Response(serialized_itinerary.data, 200)


    def post(self, request):
        serialized_itinerary = ItinerarySerializer(data=request.data)

        if serialized_itinerary.is_valid():
            serialized_itinerary.save(owner=request.user)
            return Response(serialized_itinerary.data, 201)

        return Response(serialized_itinerary.errors, 422)    



class ItineraryDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_itinerary(self, request, itinerary_id):
        try:
            itinerary = (
                Itinerary.objects.prefetch_related("itinerarylocation_set__location")
            .select_related("owner") 
            .get(id=itinerary_id)
        )
            self.check_object_permissions(request, itinerary)
            return itinerary
        except Itinerary.DoesNotExist:
            raise NotFound("Itinerary not found")

# get itinerary
    def get(self, request, itinerary_id):
        itinerary = self.get_itinerary(request, itinerary_id)
        serialized_itinerary = PopulatedItinerarySerializer(itinerary)
        return Response(serialized_itinerary.data, 200)

# edit itinerary
    def patch(self, request, itinerary_id):
        itinerary = self.get_itinerary(request, itinerary_id)
        serialized_itinerary = ItinerarySerializer(itinerary, data=request.data, partial=True)

        if serialized_itinerary.is_valid():
            serialized_itinerary.save()
            return Response(serialized_itinerary.data, 201)

        return Reponse(serialized_itinerary.errors, 422)

# delete itinerary
    def delete(self, request, itinerary_id):
        itinerary = self.get_itinerary(request, itinerary_id)
        itinerary.delete()
        return Response(status=204)


class ItineraryLocationDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]      

    def get_itinerary(self, request, itinerary_id):
        try:
            itinerary = Itinerary.objects.get(id=itinerary_id)
            self.check_object_permissions(request, itinerary)
            return itinerary
        except Itinerary.DoesNotExist as err:
            raise NotFound("Itinerary not found")    


# add location to itinerary
    def post(self, request, itinerary_id):
        itinerary = self.get_itinerary(request, itinerary_id)
        location_id = request.data.get("location_id")

        if not location_id:
            return Response({"error": "location_id is required"}, status=400)

        try:
            location = Location.objects.get(id=location_id)
        except Location.DoesNotExist:
            raise NotFound("Location not found")

        visit_date = request.data.get("location_visit_date", None)

        itinerary_location, created = ItineraryLocation.objects.get_or_create(
            itinerary=itinerary,
            location=location,
            defaults={"location_visit_date": visit_date}
        )

        if not created:
            itinerary_location.location_visit_date = visit_date
            itinerary_location.save()

        serialized_location_itinerary = ItineraryLocationSerializer(itinerary_location)
        return Response(serialized_location_itinerary.data, 201)



# edit location visit date 
    def patch(self, request, itinerary_id, location_id):
        
        itinerary = self.get_itinerary(request, itinerary_id)
        if not itinerary:
            return Response({"error": "Itinerary not found"}, status=404)

        try:
            itinerary_location = ItineraryLocation.objects.get(
                itinerary=itinerary,
                location_id=location_id
            )
        except ItineraryLocation.DoesNotExist:
            raise NotFound("Location not found in itinerary")

        visit_date = request.data.get("location_visit_date", None)

        itinerary_location.location_visit_date = visit_date
        itinerary_location.save()

        serialized_data = ItineraryLocationSerializer(itinerary_location)
        return Response(serialized_data.data, status=200)



# remove location from itinerary
    def delete(self, request, itinerary_id, location_id):
        itinerary = self.get_itinerary(request, itinerary_id)

        try:
            itinerary_location = ItineraryLocation.objects.get(
                itinerary=itinerary,
                location_id=location_id
            )
            itinerary_location.delete()
            return Response({ "message": "Location removed from itinerary" })
        except ItineraryLocation.DoesNotExist:
            raise NotFound("Location not found in itinerary")
