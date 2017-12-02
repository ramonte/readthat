from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^', include('core.urls')),
    url(r'^admin/', admin.site.urls),
]
