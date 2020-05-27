from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from trips.models import Trip
from .models import Profile, Order
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addwishlist(request, trip_id):
    # Profile = get_object_or_404(Trip, pk=trip_id)
    # Profile.wishlist.wishlist.add()
    profile = Profile.objects.get(user=request.user)
    wishlist_trip = Trip.objects.get(pk=trip_id)

    # profile.wishlist.objects.all()   #get all the wishlist in profile (to read) (maybe no need .object)

    profile.wishlist.add(wishlist_trip)
    # profile.wishlist.save()
    # request.user.wishlist.all(wishlist_trip)
    # userwishlist = Profile.wishlist(wishlist = wishlist_trip)
    # userwishlist.save()
    print(wishlist_trip)
    
    return redirect(reverse('home_route'))

@login_required
def order_history(request):
    profile = Profile.objects.get(user=request.user)
    orders = profile.orders.all()

    return render(request, 'useraccount/history.template.html', {
        "orders": orders
        })