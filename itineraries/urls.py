from django.urls import path
from .views import ItineraryListView, ItineraryDetailView, ItineraryLocationDetailView

urlpatterns = [
    path('', ItineraryListView.as_view()),
    path('<int:itinerary_id>/', ItineraryDetailView.as_view()),
    path('<int:itinerary_id>/locations/<int:location_id>', ItineraryLocationDetailView.as_view()),

]
