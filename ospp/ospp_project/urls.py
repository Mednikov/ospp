from django.conf.urls import include, url
from django.contrib import admin

from ospp_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ospp_app.urls')),
]
