from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TripForm
from .models import Trip
from django.db.models import Q

def trip_list(request):
    query = request.GET.get('q')  # single search input
    if query:
        trips = Trip.objects.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query)
        ).order_by('-created_at')
    else:
        trips = Trip.objects.all().order_by('-created_at')

    context = {'trips': trips, 'query': query}
    return render(request, 'trips/trip_list.html', context)

@login_required(login_url='login')
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'trips/add_trip.html', {'form': form})


@login_required(login_url='login')
def edit_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm(instance=trip)
    return render(request, 'trips/add_trip.html', {'form': form, 'edit': True})

@login_required(login_url='login')
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')
    return render(request, 'trips/delete_trip.html', {'trip': trip})
