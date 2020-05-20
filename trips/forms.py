from django import forms
from .models import Trip
from pyuploadcare.dj.forms import ImageField

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('location', 'date', 'price', 'accommodation', 'vendors', 'image')

