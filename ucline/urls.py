"""ucline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import patterns as patterns
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns 

from rest_framework import routers

from redsocial import views
from redsocial.views import *

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

postcanal_creation = views.CanalViewsSet.as_view({
    'post': 'set_post'
})

#
#******************************************************
#
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewsSet)
router.register(r'area_conocimiento', Area_ConocimientoViewsSet)

router.register(r'timeline', TimelineViewSet)

router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'like', LikesViewSet)
router.register(r'resource', ResourceViewSet)

#router.register(r'canal', CanalViewsSet)




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^entities/', include(router.urls)),
    url(r'^post/(?P<pk>[0-9]+)/comment/', comment_creation),
    url(r'^', include('redsocial.urls')),
    #-----Canal urls-------------------------
    url(r'^entities/canal/', canal_list, name='canal_list'), 
    url(r'^entities/canal/(?P<pk>[0-9]+)/', canal_detail, name='canal_detail'), 
    url(r'^entities/canal/(?P<pk>[0-9]+)/post/', postcanal_creation, name='postcanal_creation'),
]

urlpatterns += staticfiles_urlpatterns()

