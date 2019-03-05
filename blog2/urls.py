#!/usr/bin/python
# -*- coding:utf-8 -*-


from django.contrib import admin
from django.urls import include, path, re_path

from .views import index

urlpatterns = [
    re_path('^$', index),
]
