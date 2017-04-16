
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vacanse/' , include('vacanse.urls')),
    url(r'^shop/' , include('shop.urls')),
    url(r'^', include('news.urls')),
    url(r'^reg/', include('reg.urls'))
]
