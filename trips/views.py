from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
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

# def update_trip(request, trip_id):
#     updating_trip = get_object_or_404(Trip, pk=trip_id)
#     create_form = TripForm(instance=updating_trip)
#     return render(request, 'trips/update.template.html', {
#         "form": create_form
#     })


def update_trip(request, trip_id):
    # 1. retrieve the book that we are editing
    updating_trip = get_object_or_404(Trip, pk=trip_id)

    # 2. if the update form is submitted
    if request.method == "POST":

        # 3. create the form and fill in the user's data. Also specify that
        # this is to update an existing model (the instance argument)
        update_form = TripForm(request.POST, instance=updating_trip)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'trips/update.template.html', {
                "form": update_form
            })
    else:
        # 4. create a form with the book details filled in
        update_form = TripForm(instance=updating_trip)
        return render(request, 'trips/update.template.html', {
            "form": update_form
        })