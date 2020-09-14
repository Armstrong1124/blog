# coding=utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import pytz
from datetime import datetime
# Create your models here.


tz = pytz.timezone('Asia/Shanghai')


class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name='类别')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = '类别'

    def __str__(self):
        return 'Category: %s' % self.cname


class Tag(models.Model):
    tname = models.CharField(max_length=30, unique=True, verbose_name='标签')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = '标签'

    def __str__(self):
        return 'Tag: %s' % self.tname


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='主题')
    brief = models.TextField()
    # content = models.TextField(verbose_name='内容')
    content = RichTextUploadingField(null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now(tz))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = '主题'

    def __str__(self):
        return 'Post: %s' % self.title

