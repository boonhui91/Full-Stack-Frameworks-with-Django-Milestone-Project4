from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from trips.models import Trip
from .models import Profile, Order
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addwishlist(request, trip_id):
    profile = Profile.objects.get(user=request.user)
    wishlist_trip = Trip.objects.get(pk=trip_id)
    profile.wishlist.add(wishlist_trip)

    return redirect(reverse('home_route'))


@login_required
def viewwishlist(request):
    profile = Profile.objects.get(user=request.user)
    wishlist = profile.wishlist.all()

    return render(request, 'useraccount/wishlist.template.html', {
        'wishlist':wishlist
        })



@login_required
def order_history(request):
    profile = Profile.objects.get(user=request.user)
    orders = profile.orders.all()

    return render(request, 'useraccount/history.template.html', {
        "orders": orders
        })