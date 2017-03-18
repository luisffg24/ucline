
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns 
from django.contrib.auth.views import login
from rest_framework import routers

from redsocial import views
from redsocial.views import *


from redsocial.views import index

comment_creation = views.PostViewSet.as_view({
    'post': 'set_comment'
})

#
#****************METHODS CANAL*************************
#
canal_list = views.CanalViewsSet.as_view({
    'get': 'list',
    'post': 'create'
})

canal_detail = views.CanalViewsSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

#---------------------------------------------

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_creation = views.PostViewSet.as_view({
    'post': 'set_comment',
})

#
#******************************************************
#
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewsSet)
router.register(r'area_conocimiento', Area_ConocimientoViewsSet)
router.register(r'follow', FollowViewSet)
router.register(r'post', PostViewSet)
router.register(r'permiso', PermisosViewSet)
router.register(r'like', LikesViewSet)
router.register(r'resource', ResourceViewSet)

router.register(r'canal', CanalViewsSet)


urlpatterns = [

    #url(r'^admin/', admin.site.urls),
    url(r'^entities/', include(router.urls)),
    url(r'^index',index),
    url(r'^redsocial/', include('redsocial.urls')),
    url(r'^$',login,{'template_name':'login.html'}, name='login'),

    url(r'^v1/entities/$', post_list, name='post_list'),
    url(r'^v1/entities/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    #url(r'^v1/entities/(?P<pk>[0-9]+)/comment/$', comment_creation, name='comment_creation'),


   # url(r'^post/(?P<pk>[0-9]+)/comment/', comment_creation),
    #url(r'^', include('redsocial.urls')),
    #-----Canal urls-------------------------
    #url(r'^entities/canal/', canal_list, name='canal_list'), 
    #url(r'^entities/canal/(?P<pk>[0-9]+)/', canal_detail, name='canal_detail'), 
    #url(r'^entities/canal/(?P<pk>[0-9]+)/post/', postcanal_creation, name='postcanal_creation'),
    #url(r'^entities/post/(?P<id_post>[0-9]+)/comments$', comment_Post, 'comment_Post'),
    #url(r'^entities/profile/(?P<owner>[0-9]+)$', ProfileDetalle),



]

urlpatterns += staticfiles_urlpatterns()