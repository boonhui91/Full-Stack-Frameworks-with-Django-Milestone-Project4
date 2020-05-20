from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Trip
from .forms import TripForm

# Create your views here.
def index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.template.html',{
        'trips':trips
    })
    
    
def create_trip(request):
    # 2. if the update form is submitted
    if request.method == "POST":

        create_form = TripForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'trips/create.template.html', {
                "form": create_form
            })
    else:
        create_form = TripForm()
        return render(request, 'trips/create.template.html', {
            "form": create_form
        })
