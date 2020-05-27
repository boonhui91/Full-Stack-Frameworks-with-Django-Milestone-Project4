from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip

# Create your models here.


class Orders(models.Model):
    transaction_id = models.CharField(blank=False, max_length=100)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.transaction_id


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(Trip)
    orders = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name