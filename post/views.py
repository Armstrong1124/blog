from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator
from django.db import connection
# Create your views here.


def query_post(request, num=1):
    post_list = Post.objects.all().order_by('-create_time')
    paginator = Paginator(post_list, 2)
    num = int(num)
    print(num)
    current_page = paginator.page(num)
    # print(current_page.index())
    begin = num - 5 if num > 5 else 1
    end = begin + 9 if begin + 9 < paginator.num_pages else paginator.num_pages
    page_list = range(begin, end + 1)
    return render(request, 'index.html', {'current_page': current_page, 'page_list': page_list, 'current_num': num})


def read(request, num):
    num = int(num)
    post = Post.objects.filter(id=num)[0]
    return render(request, 'post.html', {'post': post})


def category_post(request, cid, num=1):
    post_list = Post.objects.filter(category_id=cid).order_by('-create_time')
    paginator = Paginator(post_list, 2)
    num = int(num)
    print(num)
    current_page = paginator.page(num)
    # print(current_page.index())
    begin = num - 5 if num > 5 else 1
    end = begin + 9 if begin + 9 < paginator.num_pages else paginator.num_pages
    page_list = range(begin, end + 1)
    return render(request, 'category_post.html', {'current_page': current_page,
                                                  'page_list': page_list,
                                                  'current_num': num,
                                                  'cid': cid})


def archive_post(request, year, month, num=1):
    post_list = Post.objects.filter(create_time__year=year).filter(create_time__month=month).order_by('-create_time')
    tim = year + '-' + month
    paginator = Paginator(post_list, 2)
    num = int(num)
    print(num)
    current_page = paginator.page(num)
    # print(current_page.index())
    begin = num - 5 if num > 5 else 1
    end = begin + 9 if begin + 9 < paginator.num_pages else paginator.num_pages
    page_list = range(begin, end + 1)
    return render(request, 'archive_post.html', {'current_page': current_page,
                                                 'page_list': page_list,
                                                 'tim': tim,
                                                 'current_num': num})
