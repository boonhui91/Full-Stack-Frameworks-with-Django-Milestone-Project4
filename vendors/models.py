from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(blank=False, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(blank=False, max_length=255)
    tel = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
