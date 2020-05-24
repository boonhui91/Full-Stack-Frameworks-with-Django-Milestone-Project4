from django.db import models
from vendors.models import Vendor
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.


class Accom(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(blank=False, max_length=100)
    location = models.CharField(blank=False, max_length=100)
    date = models.DateField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    accommodation = models.ForeignKey(Accom, on_delete=models.SET_NULL, null=True)
    vendors = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    image = ImageField(blank=False, manual_crop="")
    desc = models.CharField(blank=False, max_length=500)

    def __str__(self):
        return 'DiveTrip: ' + self.location
