# cleandesignuk/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('gallery/', include('project_gallery.urls', namespace='gallery')),
    path('services/', include('packages_services.urls', namespace='services')),
    path('contact/', include('contact.urls', namespace='contact')),
]
