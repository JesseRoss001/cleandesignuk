from django.urls import path
from . import views

app_name = 'developer_store'  # Define the application namespace here

urlpatterns = [
    path('', views.index, name='index'),
    path('templates/', views.templates_list, name='templates_list'),
    path('components/', views.components_list, name='components_list'),
    # More paths as needed
]
