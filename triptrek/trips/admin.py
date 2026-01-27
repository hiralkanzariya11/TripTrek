from django.contrib import admin
from .models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'start_date', 'created_at')
    list_filter = ('location', 'start_date')
    search_fields = ('title', 'location')
