#!/usr/bin/env python
# -*- coding: utf-8 -*-
from post.models import *
from django.db.models import Count
from django.db import connection


def get_right_info(request):
    # Post.objects.group_by('category__cname', 'category').annotate(c=Count('*'))
    r_catepost = Post.objects.values('category__cname', 'category').annotate(c=Count('category__cname')).order_by('-c')
    r_page = Post.objects.all().order_by('-create_time')[:3]
    cursor = connection.cursor()
    sql = "SELECT date_format(create_time,'%Y-%m'),count(*) FROM t_post" \
          " group by date_format(create_time,'%Y-%m') order by date_format(create_time,'%Y-%m') desc;"
    cursor.execute(sql)
    r_file = cursor.fetchall()
    return {'r_catepost': r_catepost, 'r_page': r_page, 'r_file': r_file}

