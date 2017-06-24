from django.conf.urls import url

from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^show$', views.show),
    url(r'^process$', views.process)
]

