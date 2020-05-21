from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(Trip)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
