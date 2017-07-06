from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^secrets$', views.secrets),
    url(r'^like/(?P<id>\d+)$', views.newlike),
    url(r'^popular$', views.popular),
    url(r'^process$', views.process),
    url(r'^logout$', views.process)
]