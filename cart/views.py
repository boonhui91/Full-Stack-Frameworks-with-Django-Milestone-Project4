from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponseForbidden
from trips.models import Trip

# Create your views here.

SHOPPING_CART = "shopping_cart"

def add_cart(request, trip_id):
    cart = request.session.get(SHOPPING_CART, {})
    # trip = get_object_or_404(Trip, pk=trip_id)
    trip = get_object_or_404(Trip, pk=trip_id)

    if trip_id not in cart:

        cart[trip_id] = {
            'id': trip_id,
            'location': trip.location,
            'qty': 1
        }
    else:
        cart[trip_id]['qty'] += 1
    request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))




def view_cart(request):
    cart = request.session.get(SHOPPING_CART)

    return render(request, 'cart/view.template.html',{
        'cart' : cart
    })


def delete_item(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:
        del cart[trip_id]
        # cart[trip_id]['qty'] -= 1
        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))


def delete_qty(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:
        cart[trip_id]['qty'] -= 1
        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))

def add_qty(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:
        cart[trip_id]['qty'] += 1
        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))