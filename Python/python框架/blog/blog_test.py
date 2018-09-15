# -*- coding: utf-8 -*-
import os,django
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()
from blog_app.models import Blog,Author,Entry

# b=Blog(name='xiaohan001 Blog',tagline='the latest news in here.')
# b.save()

#Queryset创建对象的方法
'''第一种'''
# Author.objects.create(name='weizhengtian12344',email='eamil@126.com')

'''第二种'''
# twz=Author(name='weizhengtian01',email='eamil001@126.com')
# twz.save()

'''第三种'''
# ms=Author()
# ms.name='xiongba'
# ms.email='xiongba@126.com'
# ms.save()

'''第四种   首先尝试获取，如果不存在，则创建，防止重复'''
# s=Author.objects.get_or_create(name='weizhengtian',email='eamil@126.com')
# print(s)
#

entry=Entry.objects.get()
cheese_blog=Blog.objects.get(name='xiaohan001 Blog')
entry.blog=cheese_blog
entry.save()
