from django.db import models
from locations.models import Location

# Create your models here.
class Itinerary(models.Model):
    trip_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    locations = models.ForeignKey(
        to = Location,
        on_delete=models.CASCADE,
        related_name='itineraries'
        )
    trip_start_date = models.DateField()
    trip_end_date = models.DateField()

    def __str__(self):
        return f'{self.trip_name}: {self.trip_start_date} - {self.trip_end_date}'
    