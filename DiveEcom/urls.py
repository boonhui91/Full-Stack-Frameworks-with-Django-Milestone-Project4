"""DiveEcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import trips.views
import vendors.views
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('vendors/', trips.views.read_create_trip, name = 'index_trip_route'),
    path('trips/update/<trip_id>', trips.views.update_trip, name = 'update_trip_route'),
    path('trips/delete/<trip_id>', trips.views.delete_trip, name = 'delete_trip_route'),
    path('vendors/', vendors.views.index),
    path('home/', home.views.display_home, name='home_route'),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls'))
]
