from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip

class Booking(models.Model):
    STATUS_CHOICES = (
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('PENDING', 'Pending'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_people = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.user.username} - {self.trip.title}"
