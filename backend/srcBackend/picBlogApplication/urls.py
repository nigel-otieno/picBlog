from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^feed$', views.feed),
    url(r'^profile$', views.profile),
    path('accounts/', include('allauth.urls')),

]