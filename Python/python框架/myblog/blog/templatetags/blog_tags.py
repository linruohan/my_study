from ..models import Post,Category
from django import template
from django.shortcuts import render,get_object_or_404
register=template.Library()
#最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')
#分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post'))

@register.simple_tag
def get_posts_nums_by_ym(year,month):
    return  Post.objects.filter(created_time__year=int(year),
                                    created_time__month=int(month)
                                    )