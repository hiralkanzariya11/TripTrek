from django.contrib import admin
from .models import Trip, TripImage

class TripImageInline(admin.TabularInline):
    model = TripImage
    extra = 3  # number of image fields shown by default

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    inlines = [TripImageInline]
    list_display = ('title', 'location', 'price', 'start_date')

admin.site.register(TripImage)