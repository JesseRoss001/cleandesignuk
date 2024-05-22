# project_gallery/views.py
from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'project_gallery/index.html', {
        'title': 'Project Gallery',
        'projects': projects
    })