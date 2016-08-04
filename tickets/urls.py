from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'costa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/$', views.ticket_create),
    url(r'^list/$', views.ticket_list),
    url(r'^update/(?P<id>[0-9])/$', views.ticket_update, name="update"),
    
]
