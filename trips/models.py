from django.db import models
from vendors.models import Vendor
from django.contrib.auth.models import User

# Create your models here.


class Accom(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name


class Trip(models.Model):
    # resort = 'resort'
    # lob = 'liveaboard'
    # Accom_type = (
    #         (resort, 'Resort'),
    #         (lob, 'Liveaboard'),
    #     )

    # location: models.CharField (blank=False, max_length=100)
    # date: models.DateField (blank=False)
    # price: models.DecimalField (blank=False, decimal_places=2)
    # accommodation: models.CharField(blank=False, choices=Accom_type)

    location = models.CharField(blank=False, max_length=255)
    date = models.DateField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    accommodation = models.ForeignKey(Accom, on_delete=models.SET_NULL, null=True)
    vendors = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'DiveTrip: ' + self.location

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(blank=False, max_length=30)
    lastName = models.CharField(blank=False, max_length=30)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


