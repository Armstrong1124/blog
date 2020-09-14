#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, re_path
from post import views


urlpatterns = [
    path('', views.query_post),
    re_path(r'page/(\d+)', views.query_post),
    re_path(r'post/(\d+)', views.read),
    re_path(r'category/(\d+)/(\d+)', views.category_post),
    re_path(r'archive/(\d{4})-(\d{2})/(\d+)', views.archive_post),
]
