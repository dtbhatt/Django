from django.conf.urls import url

from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^remove/(?P<id>\d+)$', views.remove)
]