__author__ = 'Pavel Mednikov'
from django.conf.urls import include, url
from ospp_app import views

urlpatterns = [
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^archive/$', views.archive, name='archive'),
]
