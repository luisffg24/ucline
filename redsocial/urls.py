from django.conf.urls import include, url
from redsocial.views import *

#from redsocial.views import UserAPI
from redsocial.views import index
from redsocial.views import registro
from redsocial.views import perfil
from redsocial.views import canales
from redsocial.views import canal

urlpatterns = [
    #url(r'^api',UserAPI.as_view(),name='api'),
    url(r'^index',index),
    url(r'^registro',registro),
    url(r'^perfil',perfil),
    url(r'^canales',canales),
    url(r'^canal',canal),
    url(r'^usuario',usuario),
    url(r'^admin', admin)
 
]



