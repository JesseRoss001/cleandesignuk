from django.db import models
from django.utils.translation import gettext_lazy as _

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time_slot = models.TimeField()
    is_available = models.BooleanField(default=True, verbose_name=_("Available"))

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"{self.full_name} ({self.date} at {self.time_slot} - {status})"
