# -*- coding: utf-8 -*-
import os,django
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_spider.settings")
django.setup()
from django.urls import reverse


url=reverse('add')
print(url)
url1=reverse('add1',args=(444,544))
print(url1)
url2=reverse('add2',args=(444,544))
print(url2)
