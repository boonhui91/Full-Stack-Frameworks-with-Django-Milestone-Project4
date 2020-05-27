from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip

# Create your models here.


class Order(models.Model):
    transaction_id = models.CharField(blank=False, max_length=100)
    total_cost = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.transaction_id


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(Trip)
    orders = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name