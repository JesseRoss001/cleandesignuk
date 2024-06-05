# developer_store/views.py

from django.shortcuts import render
from .models import Template, Component

def index(request):
    return render(request, 'developer_store/index.html')

def templates_list(request):
    templates = Template.objects.all()
    return render(request, 'developer_store/templates_list.html', {'templates': templates})

def components_list(request):
    components = Component.objects.all()
    return render(request, 'developer_store/components_list.html', {'components': components})
