from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Trip
from .forms import TripForm
from django.contrib.auth.decorators import login_required, user_passes_test


# def group_required(arg_name):
#     def decorator(view):
#         def wrapper(request, *args, **kwargs):
#             group_id = kwargs.get(arg_name)
#             user = request.user
#             if group_id in user.groups.values_list('id', flat=True):
#                 return view(request, *args, **kwargs)
#             else:
#                 return redirect(reverse('home_route'))
#         return wrapper
#     return decorator


def all_trip(request):
    trips = Trip.objects.all()
    return render(request, 'trips/alltrip.template.html', {
            'trips':trips
        })



@login_required
# @group_required('vendor')
def read_create_trip(request):
    trips = Trip.objects.all()
    if request.method == "POST":

        create_form = TripForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(read_create_trip))
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

@login_required
# @group_required('vendor')
def update_trip(request, trip_id):
    updating_trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == "POST":
        update_form = TripForm(request.POST, instance=updating_trip)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse(read_create_trip))
        else:
            return render(request, 'trips/update.template.html', {
                "form": update_form
            })
    else:
        update_form = TripForm(instance=updating_trip)
        return render(request, 'trips/update.template.html', {
            "form": update_form
        })

@login_required
# @group_required('vendor')
def delete_trip(request, trip_id):
    trip_to_delete = get_object_or_404(Trip, pk=trip_id)
    if request.method == 'POST':
        trip_to_delete.delete()
        return redirect(read_create_trip)
    else:
        return render(request, 'trips/delete.template.html', {
            "trip": trip_to_delete
        })