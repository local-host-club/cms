"""cms URL Configuration
"""
from . import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static

urlpatterns = [
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('apps.lh_auth.urls')),
    url(r'^edu/', include('apps.edu.urls')),
    url(r'^accounts/', include('allauth.urls')), ]
