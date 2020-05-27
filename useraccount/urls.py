from django.urls import path, include
import useraccount.views

urlpatterns = [
    path('history/', useraccount.views.order_history, name='history'),
   
]
