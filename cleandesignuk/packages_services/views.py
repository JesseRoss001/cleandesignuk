from django.shortcuts import render

def index(request):
    return render(request, 'packages_services/index.html', {
        'title': 'Services'
    })
