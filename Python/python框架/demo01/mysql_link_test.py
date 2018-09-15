# import MySQLdb

# db=MySQLdb.connect(host='193.169.100.238',port=3308,user='root',passwd='123456',db='news')
# cursor=db.cursor()
# cursor.execute('select * from appdemo_mysite')
# result=cursor.fetchall()
# cursor.close()
# for i in result:
#
#     print(result)
# db.close()
#coding:utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo01.settings")
import django,os,io,sys
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()

from appdemo.models import *
m=Mysite.objects.all()
m2=Mysite.objects.get(num=1)[:3]#限制查询结果条数
m3=Mysite.objects.all().order_by('num')#升序排列
m4=Mysite.objects.all().order_by('-num')#降序排列
m2.title='xiaomei'
m8.delete()#删除
m2.save()
print(m)
print(m3)
# m=Mysite(title='xiaohan',num=2)
# m.save()
