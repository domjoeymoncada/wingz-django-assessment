from django.db import models
from apps.user.models import User
from django.db.models import TextChoices
# Create your models here.
class RideStatus(TextChoices):
    EN_ROUTE = 'en_route', 'En Route'
    PICKING_UP = 'picking_up', 'Picking Up'
    DROPPING_OFF = 'dropping_off', 'Dropping Off'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'

class Ride(models.Model):
    rider = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='rider_rides', null=True, blank=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='driver_rides', null=True, blank=True)
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=RideStatus.choices, default=RideStatus.EN_ROUTE)

class RideEvent(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='events')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)