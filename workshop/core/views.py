# core/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(LoginRequiredMixin,  ListView):
    model = Post
    template_name = 'posts/post_list.html'
    def get_queryset(self):
        return (
            Post.objects
            .filter(publicado=True)
            .select_related('author')
            .prefetch_related('tags')
            .order_by('-published_date')
        )

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','author','tags']
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')  

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'author', 'tags']
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')    
    
class UsuarioLoginView(LoginView):
    template_name = 'usuarios/login.html'
    
def home(request,):
    return render(request, 'core/index.html')    