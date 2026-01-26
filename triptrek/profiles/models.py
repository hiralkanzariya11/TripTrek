from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles_photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
