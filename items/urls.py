from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^service$', views.service, name='service'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^man$', views.man, name='man'),
    url(r'^woman$', views.woman, name='woman'),
    url(r'^children$', views.children, name='children'),
    url(r'^post/(?P<title>[\w-]+)/$', views.post, name='post'),

]
