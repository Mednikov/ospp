from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from ospp_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ospp_app.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)