from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from ride_app.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=11, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()


class Ride(models.Model):
    EN_ROUTE = "en-route"
    PICKUP = "pickup"
    DROPOFF = "dropoff"
    STATUS_CHOICES = {
        EN_ROUTE: "En Route",
        PICKUP: "Pickup",
        DROPOFF: "Dropoff"
    }
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    id_rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rider")
    id_driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver")
    pickup_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RideEvent(models.Model):
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="ride")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

