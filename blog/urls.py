#!/usr/bin/python
# -*- coding:utf-8 -*-


from django.contrib import admin
from django.urls import include, path, re_path

from .views import index, article_page

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^article/(?P<article_id>[0-9]+)$', article_page),
]
