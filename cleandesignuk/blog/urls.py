# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # Additional blog-specific paths can be added here
]