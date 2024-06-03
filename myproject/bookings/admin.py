from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'time_slot', 'is_available')
    list_filter = ('date', 'is_available')
    search_fields = ('full_name', 'email', 'phone_number')

admin.site.register(Booking, BookingAdmin)
