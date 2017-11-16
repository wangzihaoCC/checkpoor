#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views,select,search2,view

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^list$',view.reachget, name='reachget'),
]

