from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.urls import reverse

class Autor(models.Model):
    name = models.CharField(max_length=100, null = False,validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True, null = False)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 30,validators=[MinLengthValidator(2)])
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Publicación')
    author = models.ForeignKey(Autor, on_delete=models.CASCADE,verbose_name="Autor",related_name='posts')
    tags = models.ManyToManyField('Tag',related_name='posts')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']
    def clean(self):
        if len(self.title) < 5:
            raise ValidationError('EL titulo debe contener al menos 5 Letras')