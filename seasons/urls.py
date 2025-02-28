from django.urls import path
from .views import SeasonDateLocationsView

urlpatterns = [
    path('locations/', SeasonDateLocationsView.as_view()),
]