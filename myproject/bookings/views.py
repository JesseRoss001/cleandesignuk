# bookings/views.py
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib import messages
import datetime

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time_slot = form.cleaned_data['time_slot']
            if Booking.objects.filter(date=date, time_slot=time_slot, is_available=True).exists():
                booking = form.save(commit=False)
                booking.date = date
                booking.time_slot = time_slot
                booking.is_available = False
                booking.save()
                messages.success(request, 'Congratulations, you have successfully booked your free website consultation. You will receive a Google Meet invite 30 minutes before your planned booking.')
                return redirect('bookings:booking_confirmation')
            else:
                messages.error(request, 'This time slot is already booked.')
    else:
        form = BookingForm()

    today = datetime.date.today()
    week = [today + datetime.timedelta(days=i) for i in range(7)]
    slots = ['14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']
    availability = {date: {slot: Booking.objects.filter(date=date, time_slot=slot, is_available=True).exists() for slot in slots} for date in week}

    return render(request, 'bookings/booking_form.html', {'form': form, 'availability': availability})

def booking_confirmation(request):
    return render(request, 'bookings/booking_confirmation.html')
