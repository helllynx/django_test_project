from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.news_index, name='news_index'),
    url(r'^(?P<id>[0-9]+)/$', views.news_detail, name='news_detail'),
    url(r'^vacancy/$', views.vacancy_index, name='vacancy_index'),
    url(r'^vacancy/(?P<id>[0-9]+)/$', views.vacancy_detail, name='vacancy_detail'),
    url(r'^shop/$', views.shop_index, name='shop_index'),
    url(r'^shop/(?P<id>[0-9]+)/$', views.shop_detail, name='shop_detail'),
]
