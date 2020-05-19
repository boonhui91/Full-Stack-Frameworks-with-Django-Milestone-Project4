from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name
