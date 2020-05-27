from django.urls import path, include
import useraccount.views

urlpatterns = [
    path('history/', useraccount.views.order_history, name='history'),
    path('wishlist/', useraccount.views.viewwishlist, name='view_wishlist'),
    path('addwishlist/<trip_id>', useraccount.views.addwishlist, name='add_wishlist'),
    path('deletewishlist/<trip_id>', useraccount.views.deletewishlist, name='delete_wishlist'),
   
]
