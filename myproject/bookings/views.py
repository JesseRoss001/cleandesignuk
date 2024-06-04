from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

def booking_view(request):
    availability = get_availability_data()
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings:booking_success')
    return render(request, 'bookings/booking_template.html', {'form': form, 'availability': availability})

def get_availability_data():
    # Logic to fetch availability data
    return {}
def submit_booking_view(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bookings:booking_success')
    return render(request, 'bookings/booking_template.html', {'form': form})


def booking_success_view(request):
    return render(request, 'bookings/booking_confirmation.html')