# -*- coding: utf-8 -*-
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from sfspider import spider
from myweb.models import  Answer,Question,Tag
s=spider.SegmentfaultQuestionSpider('1010000002542775')

print('URL:=========>',s.url)
print('question:=========>',s.dom('h1#questionTitle').text())
print('s.content=========>',s.content)
n=0
for answer in s.answers:
    n+=1
    print('answer:'+str(n),answer)

print('/'.join(s.tags))
