from django.shortcuts import render

def handler500(request, *args, **argv):
    response = render(request, 'errors/500.html', {})
    response.status_code = 500
    return response

def handler404(request, exception, template_name="errors/404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response

def handler403(request, exception, template_name="errors/403.html"):
    response = render(request, template_name)
    response.status_code = 403
    return response

def handler400(request, exception, template_name="errors/400.html"):
    response = render(request, template_name)
    response.status_code = 400
    return response
