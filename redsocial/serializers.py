
from django.core.urlresolvers import reverse
from redsocial.models import Post, Comment, Resource, User, Profile, Area_Conocimiento, Canal
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name',)
        ordering = ('-created',)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name')


class TimelineSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
   # like = LikesSerializer.PrimaryKeyRelatedField(write_only=True, queryset=Like_Post.objects.all(), source='owner')
    #comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    class Meta:
        model = Post
        fields = ('id', 'created', 'content', 'url', 'owner', 'comments', 'likes', 'resources',)
        ordering = ('-created',)

        #         def owner(self, instance):


# return reverse('user', kwargs={'username':instance.username})




# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id','created', 'content', 'url', 'comments', 'resources', 'owner', )
#         ordering = ('-created',)

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'created', 'content', 'url', 'post', 'owner')
        ordering = ('-created',)


# def post(self, instance):
#                 return reverse('post', kwargs={'id':instance.post.id})
#
#         def user(self, instance):
#                 return reverse('user', kwargs={'username':instance.username})

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'created', 'content', 'url', 'post', 'owner')
        ordering = ('-created',)

        #         def user(self, instance):
        #                 return reverse('user', kwargs={'username':instance.username})
        #
        #         def post(self, instance):
        #                 return reverse('post', kwargs={'id':instance.post.id})


#
# *******************************************************************
#



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('owner', 'nombre', 'apellido', 'telefono', 'direccion', 'fecha_nacimiento', )


class Area_ConocimientoSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Area_Conocimiento
        fields =('id', 'nombre', 'descripcion', )

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal 
        fields = ('id', 'nombre', 'descripcion', 'created', 'owner')

