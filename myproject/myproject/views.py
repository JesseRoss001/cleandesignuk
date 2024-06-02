from django.shortcuts import render

def handler500(request, *args, **argv):
    response = render(request, 'errors/500.html', {})
    response.status_code = 500
    return response
