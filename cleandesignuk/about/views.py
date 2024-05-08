from django.shortcuts import render

def index(request):
    return render(request, 'about/index.html', {
        'title': 'About Us'
    })