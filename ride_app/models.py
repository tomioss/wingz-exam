from django.db import models


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
    pickup_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RideEvent(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

