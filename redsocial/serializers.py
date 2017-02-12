
from django.core.urlresolvers import reverse
from redsocial.models import Post, Comment, Resource, User, Profile, Area_Conocimiento,\
                                 Canal, Like_Post
from rest_framework import routers, serializers, viewsets
from rest_framework.relations import SlugRelatedField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'avatar')
        ordering = ('-created',)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'avatar')

class CommentSerializer(serializers.ModelSerializer):
    #owner = OwnerSerializer(many=True)
    class Meta:
        model = Comment
        fields = ('id', 'created', 'content', 'url', 'post', 'user')
        ordering = ('-created',)

        def user(self, instance):
            return reverse('user', kwargs={'username':instance.username})
        #
       # def post(self, instance):
        #    return reverse('post', kwargs={'id':instance.post.id})

class LikesSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Like_Post
        fields = ('post', 'owner')



class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'created', 'content', 'url', 'post', 'owner')
        ordering = ('-created',)
 

class TimelineSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    comment = serializers.RelatedField(many=True, read_only='True')
    comment = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'created', 'content', 'url', 'owner', 'comment', 'likes', 'resources')
        ordering = ('-created',)

        #def owner(self, instance):
         #   return reverse('user', kwargs={'username':instance.username})

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    resources = ResourceSerializer(many=True, read_only = True)
    likes = LikesSerializer(many=True, read_only=True, source='like')

    class Meta:
        model  = Post
        fields = ('id', 'created', 'content', 'status', 'url', 'owner', 'comments', 'like', 'resources')
        ordering = ('-created',)


#class PostSerializer(serializers.HyperlinkedModelSerializer):
 #    class Meta:
  #       model = Post
   #      fields = ('id','created', 'content', 'url', 'comments', 'resources', 'owner', )
    #     ordering = ('-created',)



# def post(self, instance):
#                 return reverse('post', kwargs={'id':instance.post.id})
#
#         def user(self, instance):
#                 return reverse('user', kwargs={'username':instance.username})



#
# *****************************PROFILE SERIALIZER'S**************************************
#
class Area_ConocimientoSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Area_Conocimiento
        fields =('id', 'nombre', 'descripcion' )


class ProfileSerializer(serializers.ModelSerializer):
    #conocimiento = Area_ConocimientoSeriaizer(many=True, read_only=True, source='profile')
    #conocimientos = serializers.RelatedField(many=True, read_only=True)
    #intereses = serializers.ManyRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ('owner', 'nombre', 'apellido', 'telefono', 'direccion',\
                  'fecha_nacimiento', 'conocimientos', 'intereses')


#
# **********************CANAL SERIALIZER'S*********************************************
#

class PostCanalSerializer(serializers.ModelSerializer):
    post = PostSerializer()


class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal 
        fields = ('id', 'nombre', 'descripcion', 'created', 'owner', 'miembro', 'postcanal')
    """ miembros = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='miembro'
    )"""

