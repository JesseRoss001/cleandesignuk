from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from datetime import datetime, timedelta

def booking_view(request):
    form = BookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        # The date and time should already be set by the form directly,
        # assuming the form fields are named correctly.
        booking.save()
        return redirect('booking_success')  # Redirect to a success page
    else:
        availability = get_availability_data()
        return render(request, 'bookings/booking_template.html', {
            'form': form,
            'availability': availability
        })


def get_availability_data():
    base_date = datetime.now()
    days = [base_date + timedelta(days=i) for i in range(7)]
    time_slots = [f"{hour}:{minute:02d}" for hour in range(14, 20) for minute in [0, 30] if not (hour == 19 and minute > 0)]

    availability = {}
    for day in days:
        date_str = day.strftime("%Y-%m-%d")
        availability[date_str] = {slot: True for slot in time_slots}  # Assume all slots are available initially

    return availability

def submit_booking_view(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bookings:booking_success')
    return render(request, 'bookings/booking_template.html', {'form': form})


def booking_success_view(request):
    return render(request, 'bookings/booking_confirmation.html')