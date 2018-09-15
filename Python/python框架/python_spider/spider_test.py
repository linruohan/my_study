# -*- coding: utf-8 -*-
import os,django
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_spider.settings")
django.setup()
from myweb.spider import TagSpider
t = TagSpider(u'微信')
s=t.crawl_all_pages()
print(s)
# KeyboardInterrupt # 用control-c中断运行，测试一下就行:)
# from web.models import Tag, Question
# Question.objects.all()
# Question.objects.get(pk=5).tags.all() # 数据库中id=5的question的tags
