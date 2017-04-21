
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('post.urls')),
    url(r'^reg/', include('reg.urls')),
    # url(r"^comments/", include("django.contrib.comments.urls")),

]
