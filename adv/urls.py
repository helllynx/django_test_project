from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^shop/', views.shop, name='shop'),
    url(r'^', views.vacanse, name='vacanse'),
    url(r'^vacanse/', views.vacanse, name='vacanse')
]
