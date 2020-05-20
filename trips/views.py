from django.shortcuts import render, HttpResponse
from .models import Trip

# Create your views here.
def index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.template.html',{
        'trips':trips
    })
    