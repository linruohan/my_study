"""demo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
admin.autodiscover()
from django.urls import path
from appdemo.views import *
from django.views.generic import TemplateView
from django.views.generic.list import ListView
book_list={
    'queryset':Book.objects.all,
    'template_name':'1.html'
}

#login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello),
    path('d/',TemplateView.as_view(template_name='tongyongshitu.html')),
    path('s/',ListView.as_view(**book_list)),
    path('l/',BookListView.as_view()),
    # path('hello/',views),
    path('hello/0',base),
    path('hello/1',hour),
    path('hello/2',hour2),
    path('hello/3',current_datetime),
    path(r'hello/(\d+)',hello1),
]
# logout
urlpatterns += [
    path('li/', hello,{'template_name':'1.html'}),
    path('li/', hello,{'template_name':'2.html'}),
    path('li/', hello,{'template_name':'3.html'}),
]
# #公共事件
urlpatterns += [
    path('li/', views002(views3)),
    path('li/', views002(views2)),
]
