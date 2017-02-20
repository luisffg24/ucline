
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

urlpatterns = patterns([

    url(r'^admin/', admin.site.urls),
    url(r'^entities/', include(router.urls)),
    url(r'^post/(?P<pk>[0-9]+)/comment/', comment_creation),
    #url(r'^', include('redsocial.urls')),
    #-----Canal urls-------------------------
    #url(r'^entities/canal/', canal_list, name='canal_list'), 
    #url(r'^entities/canal/(?P<pk>[0-9]+)/', canal_detail, name='canal_detail'), 
    #url(r'^entities/canal/(?P<pk>[0-9]+)/post/', postcanal_creation, name='postcanal_creation'),
])

urlpatterns = format_suffix_patterns(urlpatterns)