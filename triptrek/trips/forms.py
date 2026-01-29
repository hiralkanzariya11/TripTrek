from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            'title',
            'location',
            'description',
            'price',
            'start_date',
            'end_date',
            'available_slots',
            'cover_image'
        ]
