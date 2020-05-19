from django.contrib import admin
from .models import Trip, Accom, Profile


# Register your models here.
admin.site.register(Trip)
admin.site.register(Accom)
admin.site.register(Profile)