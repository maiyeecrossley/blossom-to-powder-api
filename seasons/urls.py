from django.urls import path
from .views import SeasonDateLocationsView, SeasonalLocationsView

urlpatterns = [
    path('locations/', SeasonDateLocationsView.as_view()),
    path('<int:season_id>/locations/', SeasonalLocationsView.as_view())
]