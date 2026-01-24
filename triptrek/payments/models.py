from django.db import models
from bookings.models import Booking

class Payment(models.Model):
    PAYMENT_STATUS = (
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('PENDING', 'Pending'),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id}"
