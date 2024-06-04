from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'time_slot', 'is_available')
    list_filter = ('date', 'is_available')

    def get_queryset(self, request):
        # Filter only available slots
        return super().get_queryset(request).filter(is_available=True)

admin.site.register(Booking, BookingAdmin)

