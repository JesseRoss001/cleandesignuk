from django.urls import path
from .views import index, facebook_page

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('facebook-page/', facebook_page, name='facebook_page'),  # New URL pattern for the Facebook page
]