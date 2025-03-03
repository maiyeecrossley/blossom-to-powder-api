from django.contrib import admin
from .models import Location
# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]

admin.site.register(Location, LocationAdmin)