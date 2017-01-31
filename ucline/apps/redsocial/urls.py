from django.conf.urls import url
from apps.redsocial.views import UserAPI

urlpatterns = [
    url(r'^api',UserAPI.as_view(),name='api'),
    