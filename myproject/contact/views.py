# contact/urls.py
from django.shortcuts import render

def index(request):
    return render(request, 'contact/index.html', {
        'title': 'Contact'
    })
