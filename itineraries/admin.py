from django.contrib import admin
from .models import Itinerary, ItineraryLocation
from locations.models import Location

class ItineraryLocationInline(admin.TabularInline):
    model = ItineraryLocation
    extra = 1
    autocomplete_fields = ["location"]

class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("trip_name", "trip_start_date", "trip_end_date", "owner")
    inlines = [ItineraryLocationInline]

# Register your models here.
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(ItineraryLocation)