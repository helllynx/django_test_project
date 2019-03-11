from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^', include('post.urls')),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'reg/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView, {'template_name': 'reg/logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup')
]