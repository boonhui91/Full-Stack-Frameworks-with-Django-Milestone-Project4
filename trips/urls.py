from django.contrib import admin
from django.urls import path, include
import trips.views


urlpatterns = [
    path('', trips.views.all_trip, name = 'all_trip_route'),
    path('update/<trip_id>', trips.views.update_trip, name = 'update_trip_route'),
    path('delete/<trip_id>', trips.views.delete_trip, name = 'delete_trip_route'),
    path('eachtrip/<trip_id>', trips.views.each_trip, name = 'each_trip'),
]