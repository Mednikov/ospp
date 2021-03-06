__author__ = 'Pavel Mednikov'
from django.conf.urls import include, url
from ospp_app import views
#from ospp_app.views import multiuploader_delete

urlpatterns = [
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/(?P<project_id>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^projects/(?P<project_id>\d+)/preview/$', views.project_preview, name='project_preview'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^settings/', views.settings, name='settings'),

]
