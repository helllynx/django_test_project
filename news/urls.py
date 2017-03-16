from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
]