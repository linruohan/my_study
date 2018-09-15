# -*- coding: utf-8 -*-
from lxml import etree
import os,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
path=str(sys.path[0])+'\\test.html'
print(path)
with open(path, 'rb') as f:
    html = f.read().decode('utf-8')


selector = etree.HTML(html)
#提取文本
content = selector.xpath('//ul[@id="useful"]/li/text()')
for each in content:
    print (each)
#提取属性
link = selector.xpath('//a/@href')
for each in link:
    print (each)
title = selector.xpath('//a/@title')
print (title[0])
