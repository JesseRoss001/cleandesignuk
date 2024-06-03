from django import forms
from .models import Booking
import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number']

    date = forms.DateField(widget=forms.SelectDateWidget)
    time_slot = forms.ChoiceField(choices=[
        ('14:00', '2:00 PM'),
        ('14:30', '2:30 PM'),
        ('15:00', '3:00 PM'),
        ('15:30', '3:30 PM'),
        ('16:00', '4:00 PM'),
        ('16:30', '4:30 PM'),
        ('17:00', '5:00 PM'),
        ('17:30', '5:30 PM'),
        ('18:00', '6:00 PM'),
        ('18:30', '6:30 PM')
    ])
    
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today() or date > datetime.date.today() + datetime.timedelta(days=7):
            raise forms.ValidationError("Date must be within the next 7 days.")
        return date
