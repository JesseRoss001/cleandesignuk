from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler500 , handler404, handler403, handler400
from django.conf import settings
from django.conf.urls.static import static
from . import views

handler500 = views.handler500
handler404 = views.handler404
handler403 = views.handler403
handler400 = views.handler400
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('home.urls', namespace='home')),
    path('about/', include('about.urls', namespace='about')),
    path('gallery/', include('project_gallery.urls', namespace='gallery')),
    path('services/', include('packages_services.urls', namespace='services')),
    path('contact/', include('contact.urls', namespace='contact')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
