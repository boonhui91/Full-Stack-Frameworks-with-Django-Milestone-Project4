from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Trip
from .forms import TripForm

# Create your views here.
# def index(request):
#     trips = Trip.objects.all()
#     return render(request, 'trips/index.template.html',{
#         'trips':trips
#     })


def index_create_trip(request):
    # 2. if the update form is submitted
    trips = Trip.objects.all()
    if request.method == "POST":

        create_form = TripForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index_create_trip))
        else:
            return render(request, 'trips/index.template.html', {
                "form": create_form,
                'trips':trips
            })
    else:
        create_form = TripForm()
        return render(request, 'trips/index.template.html', {
            "form": create_form,
            'trips':trips
        })


def update_trip(request, trip_id):
    updating_trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == "POST":
        update_form = TripForm(request.POST, instance=updating_trip)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse(index_create_trip))
        else:
            return render(request, 'trips/update.template.html', {
                "form": update_form
            })
    else:
        update_form = TripForm(instance=updating_trip)
        return render(request, 'trips/update.template.html', {
            "form": update_form
        })

def delete_trip(request, trip_id):
    trip_to_delete = get_object_or_404(Trip, pk=trip_id)
    if request.method == 'POST':
        trip_to_delete.delete()
        return redirect(index_create_trip)
    else:
        return render(request, 'trips/delete.template.html', {
            "trip": trip_to_delete
        })