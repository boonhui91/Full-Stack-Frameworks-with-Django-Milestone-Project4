from django.urls import path, include
import cart.views
from cart.views import add_cart

urlpatterns = [
    path('add_to/<trip_id>', cart.views.add_cart, name='add_to_cart_route'),
    path('view/', cart.views.view_cart, name='view_cart_route')
]
