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
            'qty': 1,
            'date': str(trip.date),
            'price': str(trip.price),
            'original_price': str(trip.price),
            'image': str(trip.image)

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

        # delete off the whole item if, item wont show as negative value
        if (cart[trip_id]['qty'] == 1):
            del cart[trip_id]
        else:
            cart[trip_id]['qty'] -= 1

            # get original price
            original_price =float(cart[trip_id]['original_price'])
            # convert last stored price from str to float
            price_float = float(cart[trip_id]['price'])
            # minus orginal price to last stored price when minus 1 qty
            updated_price = (price_float - original_price)
            # update latest price
            cart[trip_id]['price'] = str(updated_price)

        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))

def add_qty(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:
        cart[trip_id]['qty'] += 1
        
        # get original price
        original_price =float(cart[trip_id]['original_price'])
        # convert last stored price from str to float
        price_float = float(cart[trip_id]['price'])
        # adds orginal price to last stored price when plus 1 qty
        updated_price = (price_float + original_price)
        # update latest price
        cart[trip_id]['price'] = str(updated_price)

        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))
    
def update_quantity(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:
        cart[trip_id]['qty'] = int(request.POST['qty']) #converts update qty value to int, so that add and delete qty function can work

        # get original price
        original_price =float(cart[trip_id]['original_price'])
        latest_qty = int(request.POST['qty'])
        # original price multiply by updated qty
        updated_price = (original_price * latest_qty)
        # update latest price
        cart[trip_id]['price'] = str(updated_price)

        request.session[SHOPPING_CART] = cart    
    return redirect(reverse('view_cart_route'))
