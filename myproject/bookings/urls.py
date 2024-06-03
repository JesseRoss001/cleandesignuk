from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/', views.create_booking, name='create_booking'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
