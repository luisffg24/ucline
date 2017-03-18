
from django.core.urlresolvers import reverse
from redsocial.models import Post, Comment, Resource, User, Profile, Area_Conocimiento,\
                            Canal, Like_Post, Interes, Follow, Permiso
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


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('id', 'nombre', 'tipo')


class UserSerializer(serializers.ModelSerializer):
    #conocimientos = Area_ConocimientoSeriaizer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'name', 'avatar', 'conocimientos', 'permiso')
        ordering = ('-created',)

class ProfileSerializer(serializers.ModelSerializer):
    intereses = InteresesSerializer(many=False)
    #owner = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ('owner', 'nombre', 'apellido', 'telefono', 'direccion',\
                  'fecha_nacimiento', 'intereses' )
#

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'avatar')

# *****************************POST SERIALIZER'S**************************************
#
class CommentSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=False, read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='owner')

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
        fields = ('post', 'imagenes', 'audio', 'video', 'url_compartido')  #Post-recurso 
        ordering = ('-created',)

 
class PostSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=False, read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='owner')
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    likespost = LikesSerializer(many=True, read_only=True)
    #resources = ResourceSerializer(many=False, read_only=True)

    class Meta:
        model  = Post
        fields = ('id', 'created', 'content', 'status', 'url', \
                 'owner', 'ownerId', 'likespost', 'comments',)
        ordering = ('-created',)


class TimelineSerializer(serializers.ModelSerializer):
    posts = PostSerializer()
    class Meta:
        model = Post
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
        
        #def following(self, instance):    
        #   return reverse('User', kwargs={'username':instance.username})



