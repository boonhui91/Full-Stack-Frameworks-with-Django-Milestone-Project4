from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponseForbidden
from trips.models import Trip

# Create your views here.

def add_cart(request, trip_id):
    cart = request.session.get('shopping_cart', {})
    # trip = get_object_or_404(Trip, pk=trip_id)
    trip = get_object_or_404(Trip, pk=trip_id)

    if trip_id not in cart:

        cart[trip_id] = {
            'id': trip_id,
            'location': trip.location,
            'qty': 1
        }

        print('add new to cart')

    else:
        cart[trip_id]['qty'] += 1
        print('add additional to cart')

    request.session['shopping_cart'] = cart

    return redirect(reverse('home_route'))

