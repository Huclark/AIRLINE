from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # retrieve the flight id from the Flight class
    # pk means primary key
    flight = Flight.objects.get(pk=flight_id)
    # render a template, (flight.html) and pass flight
    # as input to the flight.html template
    return render(request, "flights/flight.html", {
        "flight": flight,
        # add passengers
        # note that the passengers in flight.passengers.all()
        # is the related_name
        "passengers": flight.passenger.all()
    })