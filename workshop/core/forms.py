from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'tags']

        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'author': 'Autor',
            'tags': 'Etiquetas'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese un título'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            })
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) < 5:
            raise forms.ValidationError(
                'El título debe tener al menos 5 caracteres.'
            )

        return title