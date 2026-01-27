from django.urls import path
from .views import trip_list, add_trip, edit_trip, delete_trip

urlpatterns = [
    path('', trip_list, name='trip_list'),
    path('add/', add_trip, name='add_trip'),
    path('edit/<int:trip_id>/', edit_trip, name='edit_trip'),
    path('delete/<int:trip_id>/', delete_trip, name='delete_trip'),
]
