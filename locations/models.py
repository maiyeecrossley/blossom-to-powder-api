from django.db import models
from seasons.models import Seasons
from search_tags.models import SearchTags

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    location_image = models.CharField(blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    description = models.TextField(max_length=500)
    seasons = models.ManyToManyField(
        to = Seasons,
        related_name = 'seasonal_locations')
    visit_date = models.DateTimeField(blank=True, null=True)
    search_tags = models.ManyToManyField(
        to = SearchTags,
        related_name = 'locations'
    )