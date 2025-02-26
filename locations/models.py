from django.db import models
from seasons.models import Seasons

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    location_image = models.CharField(blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    description = models.TextField(max_length=500)
    seasons = models.ForeignKey(
        to = Seasons, 
        on_delete=models.CASCADE,
        related_name='locations')
    visit_date = models.DateTimeField()
    tags = models.IntegerField()