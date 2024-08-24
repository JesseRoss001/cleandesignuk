from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/', views.booking_view, name='book_slot'),
    path('submit_to_web3forms/<int:booking_id>/', views.submit_to_web3forms, name='submit_to_web3forms'),
    path('success/', views.booking_success_view, name='booking_success'),
]
