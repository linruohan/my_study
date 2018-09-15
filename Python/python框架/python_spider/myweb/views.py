#coding=utf-8
from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
# Create your views here.
from django.urls import reverse

def home(request):
    string=u'我在学习django框架的使用'
    onelist=['HTML','css','jquery','python','django']
    mydict={'site':u'小寒家园','content':u'学习技术和方法'}
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home.html', {'List': List})
    # return render(request,'home.html',{'string':string})
    # return render(request,'home.html',{'onelist':onelist})
    # return render(request,'home.html',{'dict':mydict})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2',args=(a,b)))
