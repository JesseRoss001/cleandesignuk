from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from datetime import datetime, timedelta

def booking_view(request):
    availability = get_availability_data()
    return render(request, 'bookings/booking_template.html', {
        'availability': availability
    })

def get_availability_data():
    base_date = datetime.now()
    days = [base_date + timedelta(days=i) for i in range(7)]
    time_slots = [f"{hour}:{minute:02d}" for hour in range(14, 20) for minute in [0, 30] if not (hour == 19 and minute > 0)]
    availability = {}
    for day in days:
        date_str = day.strftime("%Y-%m-%d")
        # Assuming some external logic or data source to mark certain time slots as unavailable
        booked_slots = []  # This should be an empty list since we're not pulling from a database
        availability[date_str] = {slot: slot not in booked_slots for slot in time_slots}
    return availability

def submit_to_web3forms(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    data = {
        'access_key': '632b6ca1-33c7-4cfd-9cf8-a2d7e8a6d414',
        'subject': 'New Booking Request',
        'name': booking.full_name,
        'email': booking.email,
        'phone_number': booking.phone_number,
        'date': booking.date.strftime('%Y-%m-%d'),
        'time_slot': booking.time_slot,
        'redirect': request.build_absolute_uri(redirect('bookings:booking_success')),
    }

    return render(request, 'bookings/submit_to_web3forms.html', {'data': data})

def booking_success_view(request):
    return render(request, 'bookings/booking_confirmation.html')
