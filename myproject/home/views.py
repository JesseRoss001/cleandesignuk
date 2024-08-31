from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def facebook_page(request):
    return render(request, 'home/facebook_page.html')