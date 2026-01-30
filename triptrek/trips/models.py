from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    available_slots = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='trip_images/cover/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TripImage(models.Model):
    trip = models.ForeignKey(Trip, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trip_images/gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.trip.title}"