from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^top$', views.top, name='top'),
    url(r'^hot$', views.hot, name='hot'),
]
