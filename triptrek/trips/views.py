from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Trip, TripImage
from .forms import TripForm, TripImageForm

# -------------------------------
# Add Trip
# -------------------------------
@login_required
def add_trip(request):
    ImageFormSet = modelformset_factory(TripImage, form=TripImageForm, extra=3)  # 3 image slots
    if request.method == 'POST':
        trip_form = TripForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=TripImage.objects.none())
        if trip_form.is_valid() and formset.is_valid():
            trip = trip_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    TripImage.objects.create(trip=trip, image=image)
            messages.success(request, "Trip added successfully!")
            return redirect('trip_list')
    else:
        trip_form = TripForm()
        formset = ImageFormSet(queryset=TripImage.objects.none())

    context = {'trip_form': trip_form, 'formset': formset}
    return render(request, 'trips/add_trip.html', context)


# -------------------------------
# List all Trips
# -------------------------------
@login_required
def trip_list(request):
    trips = Trip.objects.all().order_by('-created_at')
    return render(request, 'trips/trip_list.html', {'trips': trips})


# -------------------------------
# Edit Trip
# -------------------------------
@login_required
def edit_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    ImageFormSet = modelformset_factory(TripImage, form=TripImageForm, extra=3, can_delete=True)
    
    if request.method == 'POST':
        trip_form = TripForm(request.POST, instance=trip)
        formset = ImageFormSet(request.POST, request.FILES, queryset=TripImage.objects.filter(trip=trip))
        if trip_form.is_valid() and formset.is_valid():
            trip_form.save()
            for form in formset:
                if form.cleaned_data.get('id') and form.cleaned_data.get('DELETE'):
                    form.cleaned_data.get('id').delete()
                elif form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.trip = trip
                    image.save()
            messages.success(request, "Trip updated successfully!")
            return redirect('trip_list')
    else:
        trip_form = TripForm(instance=trip)
        formset = ImageFormSet(queryset=TripImage.objects.filter(trip=trip))

    context = {'trip_form': trip_form, 'formset': formset, 'trip': trip}
    return render(request, 'trips/edit_trip.html', context)


# -------------------------------
# Delete Trip
# -------------------------------
@login_required
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        trip.delete()
        messages.success(request, "Trip deleted successfully!")
        return redirect('trip_list')
    return render(request, 'trips/delete_trip.html', {'trip': trip})
