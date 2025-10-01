from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class FlightRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('RESERVED', 'Reserved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    travel_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
