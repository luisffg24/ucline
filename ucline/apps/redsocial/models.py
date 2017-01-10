from django.db import models

# Create your models here.

#----------------USUARIO---------------
class User(models.Model):
    username = models.TextField(primary_key=True)
    password = models.TextField(models.SET_NULL, blank=True, null=True)
    email = models.TextField(unique=True)
    name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class perfil:
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    direccion = models.TextField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_egreso = models.DateField()

#-----------------MENSAJE--------------------
class Post(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Resource(models.Model):
    post = models.ForeignKey(Post, editable=True,
                             related_name='resources')
    content = models.TextField()  # Base64 Content
    content_type = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    post = models.ForeignKey(Post, editable=True,
                             related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class like_post(models.Model):
    post = models.ForeignKey(Post, editable=True, related_name='like')
    ownwr = models.ForeignKey(User, on_delete=models.CASCADE)

#----------------AREA DE CONOCIMIENTO ------------------

class area_conocimiento(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    nombre = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=200)
    usuarios = models.ManyToManyField(User)

#-----------------CANALES---------------
class Canal:
    id = models.CharField(primary_key=True)
    nombre = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    ownwr = models.ForeignKey(User, on_delete=models.CASCADE)

#------------------FOLLOW----------------
class follow:
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE)





