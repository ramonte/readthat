from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^top$', views.top, name='top'),
    url(r'^hot$', views.hot, name='hot'),
    url(r'^posts/(?P<forum_id>[0-9]+)$', views.details, name='details'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^new_post$', views.new_post, name='new_post')
]
