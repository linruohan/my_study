from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

'''第一次视图'''
# Create your views here.
# class JSONResponse(HttpResponse):
#     """An HttpResponse that renders its content into JSON"""
#     def __init__(self,data,**kwargs):
#         content=JSONRenderer().render(data)
#         kwargs['content_type']='application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)
#
# @csrf_exempt
# def snippet_list(request):
#     """list all code snippets,or cerate a new snippet"""
#     if request.method=="GET":
#         snippets=Snippet.objects.all()
#         serialezer=SnippetSerializer(snippets,many=True)
#         return JSONResponse(serialezer.data)
#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serialezer=SnippetSerializer(data=data)
#         if serialezer.is_valid():
#             serialezer.save()
#             return JSONResponse(serialezer.data,status=201)
#     return  JSONResponse(serialezer.errors,status=400)
#
#
# @csrf_exempt
# def snippet_detail(request,pk):
#     """retrieve ,update,or delete a code snippet"""
#     try:
#         snippet=Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method=='GET':
#         serializer=SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#     elif request.method=='PUT':
#         data=JSONParser().parse(request)
#         serializer=SnippetSerializer(snippet,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors,status=400)
#     elif request.method=='DELETE':
#         snippet.delete()
#         return JSONResponse(status=204)
#
'''第二次视图'''
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
#
# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
#     if request.method=='GET':
#         snippets=Snippet.objects.all()
#         serializer=SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
#     try:
#         snippet=Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method=='GET':
#         serializer=SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

'''第三次视图'''
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# class SnippetList(APIView):
#     def get(self,request,format=None):
#         snippets=Snippet.objects.all()
#         serializer=SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)
#     def post(self,request,format=None):
#         serializer=SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class SnippetDetail(APIView):
#     def get__object(self,pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk,format=None):
#         snippet=self.get__object(pk)
#         serializer=SnippetSerializer(snippet)
#         return Response(serializer.data)
#     def put(self,request,pk,format=None):
#         snippet=self.get__object(pk)
#         serializer=SnippetSerializer(snippet)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         snippet=self.get__object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# 使用混合(mixins)
# 使用基于视图的类最大的一个好处是，它允许我们快速创建可复用的行为。我们一
# 直使用的 create/retrieve/update/delete 操作将和我们创建的任何后端模型
# API视图非常相似。这些普遍的行为是通过REST框架的混合类(mixin classes)实现
# 的。 让我们看看如何通过混合类(mixin classes)组建视图。下面是我们
# 的 views.py 模型。

'''第四次视图'''
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins,generics
#
# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

'''第五次视图'''
#使用基于视图的一般类(generic class)
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     '''现在，如果我们创建snippet数据，我们没办法将用户和snippet实例联系起来。虽
#         然用户不是序列表示的部分，但是它是请求的一个属性。 我们通过重写snippet视
#         图的 .perform_create() 方法来做到，这个方法允许我们修改如何保存实例，修
#         改任何请求对象或者请求连接里的信息。 在 SnippetList 视图类中添加以下方
#         法；
#     '''
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# 我们用了REST框架的 reverse 方法为了返回高质量的URL
@api_view(('GET',))
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'snippets':reverse('snippets-list',request=request,format=format)
    })

#
# from rest_framework import renderers
# from rest_framework.response import Response
#
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderers_classes=(renderers.StaticHTMLRenderer,)
#
#     def get(self,request,*args,**kwargs):
#         snippet=self.ger__object()
#         return Response(snippet.highlighted)

from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''this viewset automatically provides 'list' and 'detail' actions'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
from rest_framework.decorators import detail_route
from rest_framework import renderers
class SnippetViewSet(viewsets.ModelViewSet):
    '''this viewset automatically provides 'list','created','retrieve','update','destroy',actions
    Additionally we also provide an extra 'highlight' action
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        snippet=self.get__object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



























