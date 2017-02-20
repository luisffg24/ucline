
from django.core.urlresolvers import reverse
from redsocial.models import Post, Comment, Resource, User, Profile, Area_Conocimiento,\
                            Canal, Like_Post, Interes, Follow
from rest_framework import routers, serializers, viewsets
from rest_framework.relations import SlugRelatedField

#
# *****************************PROFILE SERIALIZER'S**************************************
#
class Area_ConocimientoSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Area_Conocimiento
        fields =('id', 'nombre', 'descripcion' )

class InteresesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interes
        fields = ('interes')


class ProfileSerializer(serializers.ModelSerializer):
    #  intereses = InteresesSerializer()
    class Meta:
        model = Profile
        fields = ('owner', 'nombre', 'apellido', 'telefono', 'direccion',\
                  'fecha_nacimiento', 'conocimientos')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'avatar')
        ordering = ('-created',)

#
# *****************************POST SERIALIZER'S**************************************
#

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'avatar')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('created', 'content', 'url', 'post', 'owner')
        ordering = ('-created',)

       # def user(self, instance):
       #    return reverse('user', kwargs={'username':instance.username})
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
        fields = ('created', 'content', 'url', 'post', 'content_type')    
        ordering = ('-created',)

 
class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='comments'
    )    
    resources = ResourceSerializer(many=False)
    class Meta:
        model  = Post
        fields = ('created', 'content', 'status', 'url', 'resources',\
                 'owner', 'likespost', 'comments')
        ordering = ('-created',)


class TimelineSerializer(serializers.ModelSerializer):
    posts = PostSerializer()
    class Meta:
        #model = Post
        fields = ('posts')
        #fields = ('id', 'created', 'content', 'url', 'owner', 'comment', 'likes', 'resources')
        #ordering = ('-created',)

        #def owner(self, instance):
         #   return reverse('user', kwargs={'username':instance.username})



#class PostSerializer(serializers.HyperlinkedModelSerializer):
 #    class Meta:
  #       model = Post
   #      fields = ('id','created', 'content', 'url', 'comments', 'resources', 'owner', )
    #     ordering = ('-created',)




#
# **********************CANAL SERIALIZER'S*********************************************
#

class PostCanalSerializer(serializers.ModelSerializer):
    post = PostSerializer()


"""class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal 
        fields = ('id', 'nombre', 'descripcion', 'created', 'owner', 'miembro', 'postcanal')
     miembros = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='miembro'
    )"""

class CanalSerializer(serializers.ModelSerializer):
    
    postcanal = PostSerializer(many=True, read_only=True, source='set_post')
    
    class Meta:
        model = Canal
        fields = ('id', 'nombre', 'descripcion','created', 'owner', 'miembro', 'areaconocimientos', 'postcanal')

class FollowSerializer(serializers.ModelSerializer):
    following =  OwnerSerializer()

    class Meta:
        model = Follow    
        fields = ('following','created','follower',)    
        ordering = ('-created',)    
        
        def following(self, instance):    
            return reverse('user', kwargs={'username':instance.username})



