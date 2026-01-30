from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_list, name='trip_list'),             # List all trips
    path('add/', views.add_trip, name='add_trip'),           # Add a new trip
    path('edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),  # Edit a trip
    path('delete/<int:trip_id>/', views.delete_trip, name='delete_trip'),  # Delete a trip
]
