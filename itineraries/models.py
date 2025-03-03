from django.db import models
from locations.models import Location
from users.models import User

# Create your models here.
class Itinerary(models.Model):
    trip_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    locations = models.ManyToManyField(
        to = Location,
        related_name='itineraries',
        through = 'ItineraryLocation'
        )
    trip_start_date = models.DateField(blank=True, null=True)
    trip_end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(
        to = User,
        on_delete=models.CASCADE,
        related_name='itineraries',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.trip_name}: {self.trip_start_date} - {self.trip_end_date} by {self.owner}'
class ItineraryLocation(models.Model):
    itinerary = models.ForeignKey(
        to = Itinerary, 
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        to = Location,
        on_delete=models.CASCADE
    )
    location_visit_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.location.name} on {self.location_visit_date}'    

    