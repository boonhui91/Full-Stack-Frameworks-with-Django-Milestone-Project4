from django.shortcuts import render, HttpResponse, redirect, reverse
from trips.models import Trip


# Create your views here.
def display_home(request):
    trips = Trip.objects.all()
    return render(request, 'home/home.template.html',{
        'trips':trips
    })
