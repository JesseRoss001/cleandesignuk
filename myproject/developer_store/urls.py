# developer_store/urls.py

from django.urls import path
from . import views

app_name = 'developer_store'  # This is necessary to use namespace in 'include()'

urlpatterns = [
    path('', views.index, name='index'),
    path('templates/', views.templates_list, name='templates_list'),
    path('components/', views.components_list, name='components_list'),
]