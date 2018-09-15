# -*- coding: utf-8 -*-
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from sfspider import spider
s=spider.SegmentfaultTagSpider(u'微信')

s1=s.next_page
print(s1)
print(s.__getattribute__)
print('s.page:',type(s1))
n=0
# for question in s1.questions:
#     n+=1
#     id=question.split(r'/')[-1]
#     id_dic.append(id)
    # print(id)
    # print('question:'+str(n),question)
    # print('URL:=========>',s.url)
    # print('question:=========>',s.dom('h1#questionTitle').text())
    # n=0
    # id_dic=[]
    # for question in s.questions:
    #     n+=1
    #     id=question.split(r'/')[-1]
    #     id_dic.append(id)
    #     # print(id)
    #     # print('question:'+str(n),question)
    # print(id_dic)
    # # print(s.has_next_page)
    # # print(s.next_page)
    # dict={}
    # for i in id_dic:
    #     id=i
    #     s1=spider.SegmentfaultQuestionSpider(i)
    #     url=s1.url
    #     title=s1.title
    #     question=s1.content
    #     answer=[answer for answer in s1.answers]
    #     tags=s1.tags
    #     print(title)
    # s.page=s.next_page
    # s=spider.SegmentfaultTagSpider(u'微信',page=s.page)
