from django.shortcuts import render
from .models import Project

def index(request):
    # Retrieve all projects ordered by 'created_at' in descending order (newest first)
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'project_gallery/index.html', {
        'title': 'Project Gallery',
        'projects': projects
    })
