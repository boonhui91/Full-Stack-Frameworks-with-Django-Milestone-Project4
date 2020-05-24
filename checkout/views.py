from django.shortcuts import render, get_object_or_404, reverse, HttpResponse
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from trips.models import Trip
import stripe
# Create your views here.

SHOPPING_CART = "shopping_cart"

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    line_items = []

    cart = request.session.get(SHOPPING_CART, {})

    for id, trips in cart.items():
        trips_from_db = get_object_or_404(Trip, pk=id)

        line_items.append({
            'name': str(trips_from_db.location),
            'amount': int(trips_from_db.price*100),
            'currency': 'SGD',
            'quantity': trips['qty']
        })

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=domain + reverse(checkout_success),
        cancel_url=domain + reverse(checkout_cancelled)
    )

    return render(request, 'checkout/checkout.template.html',{
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    # reset the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout successful")


def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")


def handle_checkout_session(session):
    print(session)


@csrf_exempt
def payment_completed(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.SIGNING_SECRET
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    handle_checkout_session(session)

  return HttpResponse(status=200)


