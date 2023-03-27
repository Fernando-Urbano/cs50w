from django.contrib import admin

try:
    from sql.airline.flights.models import Flight
except:
    from flights.models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    
class PassengersAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights", )

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengersAdmin)