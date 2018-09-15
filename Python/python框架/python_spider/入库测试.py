# -*- coding: utf-8 -*-
'''测试未过'''
import os,django
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_spider.settings")
django.setup()
from myweb.spider import TagSpider
from myweb.models import  Tag,Question

t=TagSpider(u'微信')
print(t.crawl_all_pages())

print(Question.objects.all())

print(Question.objects.get(pk=5).tags.all())
