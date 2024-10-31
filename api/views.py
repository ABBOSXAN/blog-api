from django.shortcuts import render
from .serializers import PostSerializer
from posts.models import Post
from rest_framework import generics
# Create your views here.

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView): # detail, update, delete
    queryset = Post.objects.all()
    serializer_class = PostSerializer

