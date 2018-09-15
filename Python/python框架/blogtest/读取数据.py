#coding=utf-8
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
django.setup()
from blog.models import Category, Tag, Post
c=Category.objects.all()
t=Tag.objects.all()
p=Post.objects.all()
# print(c)
# print(t)
print(p)
post_list = Post.objects.all().order_by('-created_time')
print(post_list)
# print(post_list)
for post in post_list:
    print(post.title)
    print(post.created_time)
    print(post.excerpt)
    print(post.created_time.year)
    print(post.created_time.month)
year=2018
month=5
post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
print(post_list)
# c=u'历史'
# post_list1=Post.objects.filter(category=c)
# print(post_list1)
# for post in post_list:
#     print(post.created_time.year)
#     print(post.created_time.month)
