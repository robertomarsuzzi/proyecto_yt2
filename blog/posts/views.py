from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, PostView, Like
# Create your views here.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    fields = (  'title',
                'content',
                'created_on',
                'last_modified',
                'author',
                'slug'
    )

    
class PostCreateView(CreateView):
    model = Post
    #fields = ['title', 'content']

class PostUpdateView(UpdateView):
    model = Post
    fields = (  'title',
                'content',
                
                'author',
                'slug'
 )
    #fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'