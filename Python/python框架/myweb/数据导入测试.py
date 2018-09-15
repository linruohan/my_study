#coding:utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

from tools.models import *
import django,os,io,sys
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()


def main():
    dir=os.path.dirname(__file__)
    path=dir+'\\olddb.txt'
    print(dir,path)
    f = open(path)
    for line in f:
        title,content = line.split('****')
        print(title,content)
        # 写入表
        # Blog.objects.create(title=title,content=content)
    f.close()

if __name__ == "__main__":
    main()
    print('Done!')
