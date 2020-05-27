from django.urls import path, include
import useraccount.views

urlpatterns = [
    path('history/', useraccount.views.order_history, name='history'),
    path('wishlist/', useraccount.views.viewwishlist, name='view_wishlist'),
   
]
