from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Autor(models.Model):
    name = models.CharField(max_length=100, null = False)
    email = models.EmailField(unique=True, null = False)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Publicacion')
    author = models.ForeignKey(Autor, on_delete=models.CASCADE,verbose_name="Autor")
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']
# En el modelo Post, implementar el método clean() para validar que el título contenga al menos 5 caracteres.        
    def clean(self):
        if len(self.title) < 5:
            raise ValidationError('EL titulo debe contener al menos 5 Letras')