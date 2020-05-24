from django import forms
from .models import Trip
from pyuploadcare.dj.forms import ImageField

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('name', 'location', 'date', 'price', 'accommodation', 'vendors', 'image', 'desc')

