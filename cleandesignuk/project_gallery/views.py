from django.shortcuts import render

def index(request):
    return render(request, 'project_gallery/index.html', {
        'title': 'Project Gallery'
    })