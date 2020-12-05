from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib import admin
from .views import current_user, UserList

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^feed$', views.feed),
    url(r'^profile$', views.profile),
    url(r'^profile_edit$', views.profile_edit),
    url(r'^logout$', views.logout),
    path('accounts/', include('allauth.urls')),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]