from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profiles

class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'last_login')

admin.site.register(Profiles, ProfilesAdmin)
