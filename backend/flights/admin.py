from django.contrib import admin
from .models import FlightRequest, Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')

@admin.register(FlightRequest)
class FlightRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'destination', 'travel_date', 'status')
    list_filter = ('status', 'destination')
