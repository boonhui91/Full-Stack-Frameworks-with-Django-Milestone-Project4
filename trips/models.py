from django.db import models

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
    # accommodation: models.CharField(blank=False, choices=Accom_type)
    accommodation = models.ForeignKey(Accom, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.location

