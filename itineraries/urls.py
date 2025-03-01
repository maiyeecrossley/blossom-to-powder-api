from django.urls import path
from .views import ItineraryListView, ItineraryDetailView

urlpatterns = [
    path('', ItineraryListView.as_view()),
    path('<int:itinerary_id>/', ItineraryDetailView.as_view()),

]