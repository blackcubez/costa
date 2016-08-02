from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'costa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.poll_list, name='list' ),
    url(r'^list/(?P<id>[0-9])/$', views.poll_detail, name='detail'),
    url(r'^create/$', views.poll_create, name='create'),
]
