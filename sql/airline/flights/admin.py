from django.contrib import admin

try:
    from sql.airline.flights.models import Flight
except:
    from flights.models import Flight, Airport, Passenger

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)