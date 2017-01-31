from django.shortcuts import render
from rest_framework.views import APIView
from apps.redsocial.serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
class UserAPI(APIView):
	serializer=UserSerializer

	def get(self,request,format=none):
		lista=User.objects.all()
		response=self.serializer(lista,many=True)
		return HttpResponse(json.dumps(response.data),content_type='aplication/json')

