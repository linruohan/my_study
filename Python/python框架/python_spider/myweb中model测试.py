# -*- coding: utf-8 -*-
import os,django
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_spider.settings")
django.setup()
from myweb.models import  Answer,Question,Tag
tag=Tag()
tag.title=u'标签001'
tag.save()
print(tag)
#
#
question=Question(title=u'测试提问',content=u'提问内容')
question.save()
question.tags.add(tag)
question.save()

#
answer=Answer(content=u'回答内容',question=question)
answer.save()

print(tag.questions.all())# 根据tag找question
print(question.tags.all())# 获取question的tags
print(question.answers.all())# 获取问题的答案
