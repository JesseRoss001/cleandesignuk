from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'time_slot', 'is_available')
    list_filter = ('date', 'is_available')
    search_fields = ('full_name', 'date')
    actions = ['mark_as_unavailable', 'mark_as_available']

    @admin.action(description='Mark selected bookings as unavailable')
    def mark_as_unavailable(self, request, queryset):
        queryset.update(is_available=False)

    @admin.action(description='Mark selected bookings as available')
    def mark_as_available(self, request, queryset):
        queryset.update(is_available=True)
