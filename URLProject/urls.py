
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include, re_path
from Shortner import views
from . import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Shortner.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
