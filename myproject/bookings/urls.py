from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/', views.booking_view, name='book_slot'),
    path('submit/', views.submit_booking_view, name='submit_booking'),
    path('success/', views.booking_success_view, name='booking_success'),
]
