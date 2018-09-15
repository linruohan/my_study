from django.conf.urls import url,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns#格式后缀模式
from snippets.views import SnippetViewSet,UserViewSet,api_root
from rest_framework import renderers

# snippet_list=SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create',
# })
# snippet_detail=SnippetViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy',
# })
# snippet_highlight=SnippetViewSet.as_view({
#     'get':'highlight',},renderer_classes=[renderers.StaticHTMLRenderer])
# user_list=UserViewSet.as_view({
#     'get':'list',
# })
# user_detail=UserViewSet.as_view({
#     'get':'retrieve',
# })
#
# # API endpoints
# urlpatterns=format_suffix_patterns([
#     url(r'^$',views.api_root),
#     url(r'^snippets/$',snippet_list,name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',snippet_detail,name='snippets-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',snippet_highlight,name='snippet-highlight'),
#     url(r'^users/$',user_list,name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',user_detail,name='user-detail'),
# ])
# #login and logout views for the browsable API
# urlpatterns+=[
#     url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
# ]


from django.conf.urls import url,include
from snippets import views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
#create a router and register our viewsets with it
router=DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

#the API URLS are now determined automatically by the router
#additionally we include the login URLS for the briwsavke API
schema_view=get_schema_view(title='Pastebin API')
urlpatterns=[
    url(r'^schema/$',schema_view),
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]



























