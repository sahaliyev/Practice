from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^service/$', views.service, name='service'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^man/$', views.man, name='man'),
    url(r'^woman/$', views.woman, name='woman'),
    url(r'^children/$', views.children, name='children'),
    url(r'^login/$', views.log, name='log'),
    url(r'^logout/$', auth_views.logout, name="logout",  kwargs={'next_page': '/'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^post/(?P<title>[\w-]+)/$', views.post, name='post'),

]
