# core/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

def home(request):
    return render(request, 'core/index.html')

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'tags']
    template_name = 'posts/post_form.html'