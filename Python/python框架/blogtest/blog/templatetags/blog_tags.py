from django import template
from django.db.models.aggregates import Count
from django.shortcuts import  get_object_or_404
from ..models import Post, Category,Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month')


# 分类模板标签
@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # gt就是greate than，表示大于，不是大于等于。大于等于是gte
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gte=0)

@register.simple_tag
def get_tags():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gte=0)



@register.simple_tag
def get_posts_nums_by_ym(year, month):
    return Post.objects.filter(created_time__year=int(year),
                               created_time__month=int(month)
                               )
