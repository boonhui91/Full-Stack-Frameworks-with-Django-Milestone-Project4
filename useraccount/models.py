from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(blank=False, max_length=30)
    lastName = models.CharField(blank=False, max_length=30)
    wishlist = models.ManyToManyField(Trip)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
