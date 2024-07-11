from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, passengers

# Create your views here.

def home(request):
    """
    Renders the home page with a list of all flights.
    """
    all_flights = Flight.objects.all()
    context = {
        'flights': all_flights
    }
    return render(request, 'flights/home.html', context)

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    context = {
        'flight': flight,
        'passengers': flight.passengers.all(), # Assuming passengers are a ManyToManyField on Flight model.
        'non_passengers': passengers.objects.exclude(flights=flight).all()
    }
    return render(request, 'flights/flight.html', context)

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(id=flight_id)
        # Add passenger to flight
        passenger = passengers.objects.get(id=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight.id,)))



