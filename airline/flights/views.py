from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

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
        # the flight being rendered
        "flight": flight,
        # add passengers
        # note that the passengers in flight.passengers.all()
        # is the related_name
        "passengers": flight.passenger.all(),
        # these are passengers who are not on the flight which we will have an option to
        # register them
        # exclude(flights=flight) is to get those who are not already on the flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
    
def book(request, flight_id):
    # we are manipulating data so we wont use get but post
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        # Get the passenge whose pk = whatever that was submitter by the POST form with a name of 'passenger'
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # add a new row into a table to keep track of the passengers on that flight
        # take a passenger, take their set of flights and add a new flight to that set of flights
        passenger.flights.add(flight)
        # redirect the user back to the flight page
        # reverse takes the route as first argument which is 'flight'url
        # the 'flight' route takes the flight_id as an argument so you need to add the flight_id
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
