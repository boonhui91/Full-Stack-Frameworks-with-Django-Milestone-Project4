from django.urls import path, include
import cart.views

urlpatterns = [
    path('add/<trip_id>', cart.views.add_cart, name='add_to_cart_route'),
    path('', cart.views.view_cart, name='view_cart_route'),
    path('delete/<trip_id>', cart.views.delete_item, name='delete_cart_route'),
    path('delete-qty/<trip_id>', cart.views.delete_qty, name='delete_qty_route'),
    path('add-qty/<trip_id>', cart.views.add_qty, name='add_qty_route'),
    path('update-qty/<trip_id>', cart.views.update_quantity, name='update_qty_route')

]
