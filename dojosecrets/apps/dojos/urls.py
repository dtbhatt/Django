from django.conf.urls import url

from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^secrets$', views.secrets),
    # url(r'^post$', views.post),
    # url(r'^popular$', views.popular)
]
