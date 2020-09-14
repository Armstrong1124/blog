from django.contrib import admin
from post.models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
