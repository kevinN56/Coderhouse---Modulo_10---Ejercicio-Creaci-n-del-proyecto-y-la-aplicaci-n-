from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


# Muestra el listado de publicaciones disponibles
# Solo permite el acceso a usuarios autenticados
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'

    # Obtiene únicamente los posts publicados,
    # ordenados por fecha descendente
    def get_queryset(self):
        return (
            Post.objects
            .filter(publicado=True)
            .select_related('author')
            .prefetch_related('tags')
            .order_by('-published_date')
        )


# Muestra la información completa de un post
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


# Permite crear una nueva publicación mediante un formulario
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')


# Permite modificar una publicación existente
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')


# Permite eliminar una publicación previa confirmación
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')


# Vista encargada de la autenticación de usuarios
class UsuarioLoginView(LoginView):
    template_name = 'usuarios/login.html'


# Página principal del proyecto
# Requiere que el usuario haya iniciado sesión
@login_required
def home(request):
    return render(request, 'core/index.html')