from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_travel_plan$', views.showAdd, name = 'add_page'),
    url(r'^add_travel_plan/add$', views.addPlan, name = 'add_plan'),
    url(r'^view_plan/(?P<id>\d+)$', views.viewPlan, name = 'view_plan'),
    url(r'^join/(?P<id>\d+)$', views.join, name = 'join')

]
