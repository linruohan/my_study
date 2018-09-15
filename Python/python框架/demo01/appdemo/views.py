from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import datetime
from django.views.generic.list import ListView
from appdemo.models import *
from appdemo.forms import *

from django.core.cache import cache#缓存
from django.views.decorators.cache import cache_page
# Create your views here.
#ab -n 1000 http://localhost:8000/hello
#测试1000个链接好得资源
@cache_page(60 * 50)# 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def hello(request):
    b=Book.objects.all()
    return render_to_response('2.html',{'book':b})
# def hello(request):
#     if cache.get('book'):
#         b=cache.get('book')
#     else:
#         b=Book.objects.all()
#         cache.set('book',b)
#     return render_to_response('2.html',{'book':b})
# def hello(request):
#     b=Book.objects.get_book_count('django')
#     return render_to_response('book.html',{'book':b,'count':count})
# def hello(request):
#     if request.method=='POST':
#         form=Mybook(request.POST)
#         if form.is_valid():
#             data=form.cleaned_data
#             name=data['name']
#         return HttpResponse(name)
#
#     form=Mybook()
#     return render_to_response('req_test.html',{'form':form})


class BookListView(ListView):
    model=Book
    queryset=Book.objects.filter(title__icontains='django')
    template_name='1.html'
    def get_content_data(self,**kwargs):
        content=super(BookListView,self).get_content_data(**kwargs)
        return content

def hello1(request,num):
    try:
        num=int(num)
    except ValueError:
        raise Http404()


def views(request):
    return render_to_response('2.html')

def base(request):
    return render_to_response('base.html')

def hour(request):
    current_date = datetime.datetime.now()
    return render_to_response('hour.html', locals())

def hour2(request):
    next_time = datetime.datetime.now()
    return render_to_response('hour2.html', locals())

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('date.html', locals())



def views2(request):
    return render_to_response('1.html')
def views3(request):
    return render_to_response('2.html')


def views(request,url):
    if url=='view2':
        template_name='1.html'
    else:
        template_name='2.html'
    return render_to_response(template_name)

def views01(request,template_name):

    return render_to_response(template_name)


#公共事件
def views002(func):
    def view(request):
        #do something
        return func
    return view
