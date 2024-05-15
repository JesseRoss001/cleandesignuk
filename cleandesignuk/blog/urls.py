from django.urls import path
from .views import index, blog_detail

app_name = 'blog'  # Add this line

urlpatterns = [
    path('', index, name='blog_list'),
    path('<int:pk>/', blog_detail, name='blog_detail'),
]