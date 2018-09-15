# coding=utf-8
from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
'''定制 Admin 后台
在 admin post 列表页面，我们只看到了文章的标题，
但是我们希望它显示更加详细的信息，这需要我们来定制 Admin 了，
在 admin.py 添加如下代码：'''


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fieldsets = (
        ['Main', {
            'fields': ('title', 'created_time', 'category'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ( 'author',),
        }])


admin.site.register(Post, PostAdmin)  # 把新增的 PostAdmin 也注册进来
admin.site.register(Category)
admin.site.register(Tag)
