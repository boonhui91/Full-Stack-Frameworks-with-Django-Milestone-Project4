from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponseForbidden
from trips.models import Trip
from django.contrib.auth.decorators import login_required


# Create your views here.

SHOPPING_CART = "shopping_cart"

@login_required
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
        latest_qty = cart[trip_id]['qty']
        # get original price
        original_price =float(cart[trip_id]['original_price'])
        # convert last stored price from str to float
        price_float = float(cart[trip_id]['price'])
        # original price multiply by updated qty
        updated_price = (original_price * latest_qty)
        # update latest price
        cart[trip_id]['price'] = str(updated_price)
    request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))



@login_required
def view_cart(request):
    cart = request.session.get(SHOPPING_CART)

    if cart:
        # calculate total cart cost
        updated_total_cost = 0
        for each in cart:
            each_qty = cart[each]['qty']
            each_cost = cart[each]['price']
            updated_total_cost += float(each_cost)
            
        request.session[SHOPPING_CART] = cart

        return render(request, 'cart/viewcart.template.html',{
            'cart' : cart,
            'updated_total_cost':updated_total_cost

        })
    else:
        return render(request, 'cart/emptycart.template.html')


@login_required
def delete_item(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:
        del cart[trip_id]
        # cart[trip_id]['qty'] -= 1
        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))


@login_required
def delete_qty(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:

        # delete off the whole item if, item wont show as negative value
        if (cart[trip_id]['qty'] == 1):
            del cart[trip_id]
        else:
            cart[trip_id]['qty'] -= 1
            
            latest_qty = cart[trip_id]['qty']
            # get original price
            original_price =float(cart[trip_id]['original_price'])
            # convert last stored price from str to float
            price_float = float(cart[trip_id]['price'])
            # original price multiply by updated qty
            updated_price = (original_price * latest_qty)
            # update latest price
            cart[trip_id]['price'] = str(updated_price)

        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))


@login_required
def add_qty(request, trip_id):
    cart = request.session.get(SHOPPING_CART)
    if trip_id in cart:
        cart[trip_id]['qty'] += 1
        latest_qty = cart[trip_id]['qty']
        # get original price
        original_price =float(cart[trip_id]['original_price'])
        # convert last stored price from str to float
        price_float = float(cart[trip_id]['price'])
        # original price multiply by updated qty
        updated_price = (original_price * latest_qty)
        # update latest price
        cart[trip_id]['price'] = str(updated_price)

        request.session[SHOPPING_CART] = cart

    return redirect(reverse('view_cart_route'))

@login_required
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
