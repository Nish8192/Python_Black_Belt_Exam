from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_user$', views.createUser, name='create_user'),
    url(r'^login$', views.logIn, name='log_in'),
    url(r'^logout$', views.logOut, name='log_out'),
    # url(r'^home$', views.goHome, name='go_home'),
]
