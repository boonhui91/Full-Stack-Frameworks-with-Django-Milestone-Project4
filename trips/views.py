from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Trip
from .forms import TripForm, SearchForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q


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


def each_trip(request, trip_id):
    trips = get_object_or_404(Trip, pk=trip_id)
    
    return render(request, 'trips/eachtrip.template.html', {
        "trips": trips
        })


# for vendor access
@login_required
# @group_required('vendor')
def read_create_trip(request):
    if request.user.groups.filter(name='vendor').exists():
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
    else:
        return redirect(reverse('home_route'))

@login_required
# @group_required('vendor')
def update_trip(request, trip_id):
    if request.user.groups.filter(name='vendor').exists():
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
    else:
        return redirect(reverse('home_route'))

@login_required
# @group_required('vendor')
def delete_trip(request, trip_id):
    if request.user.groups.filter(name='vendor').exists():
        trip_to_delete = get_object_or_404(Trip, pk=trip_id)
        if request.method == 'POST':
            trip_to_delete.delete()
            return redirect(read_create_trip)
        else:
            return render(request, 'trips/delete.template.html', {
                "trip": trip_to_delete
            })
    else:
        return redirect(reverse('home_route'))


def search(request):
    trips = Trip.objects.all()

    search_form = SearchForm(request.GET)

    # always true
    queries = ~Q(pk__in=[])

    if request.GET:

        if 'search' in request.GET and request.GET['search']:
            queries = queries & (Q(name__icontains=request.GET['search']) | Q(location__icontains=request.GET['search']))

    trips = trips.filter(queries)

    if trips:
        search_result = True
    
    else:
        search_result = False

    return render(request, 'trips/search.template.html', {
                'trips':trips,
                'search_result':search_result
                })