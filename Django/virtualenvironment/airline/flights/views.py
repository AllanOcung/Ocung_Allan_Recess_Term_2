from django.shortcuts import render
from .models import Flight

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
        'passengers': flight.passengers.all()  # Assuming passengers are a ManyToManyField on Flight model.
    }
    return render(request, 'flights/flight.html', context)
