
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^env/del/(?P<id>[0-9]+)', views.env_del, name='env_del'),
    url(r'^env/edit/(?P<id>[0-9]+)', views.env_edit, name='env_edit'),
    url(r'^env/add/', views.env_add, name='env_add'),
    url(r'^env/', views.env, name='env'),

    url(r'^os/del/(?P<id>[0-9]+)', views.os_del, name='os_del'),
    url(r'^os/edit/(?P<id>[0-9]+)', views.os_edit, name='os_edit'),
    url(r'^os/add/', views.os_add, name='os_add'),
    url(r'^os/', views.os, name='os'),


    url(r'^project/del/(?P<id>[0-9]+)', views.project_del, name='project_del'),
    url(r'^project/edit/(?P<id>[0-9]+)', views.project_edit, name='project_edit'),
    url(r'^project/add/', views.project_add, name='project_add'),
    url(r'^project/auth/(?P<id>[0-9]+)', views.project_auth, name='project_auth'),
    url(r'^project/auth', views.project_auth_list, name='project_auth_list'),
    url(r'^project/', views.project, name='project'),

    url(r'^resource/del/(?P<id>[0-9]+)', views.resource_del, name='resource_del'),
    url(r'^resource/edit/(?P<id>[0-9]+)', views.resource_edit, name='resource_edit'),
    url(r'^resource/add/', views.resource_add, name='resource_add'),
    url(r'^resource/auth/(?P<id>[0-9]+)', views.resource_auth, name='resource_auth'),
    url(r'^resource/auth', views.resource_auth_list, name='resource_auth_list'),
    url(r'^resource/', views.resource, name='resource'),

    url(r'^server/del/(?P<id>[0-9]+)', views.server_del, name='server_del'),
    url(r'^server/edit/(?P<id>[0-9]+)', views.server_edit, name='server_edit'),
    url(r'^server/add/', views.server_add, name='server_add'),
    url(r'^server/', views.server, name='server'),

    url(r'^vhost/del/(?P<id>[0-9]+)', views.vhost_del, name='vhost_del'),
    url(r'^vhost/edit/(?P<id>[0-9]+)', views.vhost_edit, name='vhost_edit'),
    url(r'^vhost/add/', views.vhost_add, name='vhost_add'),
    url(r'^vhost/', views.vhost, name='vhost'),

]




