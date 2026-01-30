# forms.py
from django import forms
from .models import Trip, TripImage

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'location', 'description', 'price', 'start_date', 'end_date', 'available_slots']

class TripImageForm(forms.ModelForm):
    class Meta:
        model = TripImage
        fields = ['image']
