from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time_slot = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} - {self.date} {self.time_slot}"
