from django.shortcuts import render
from .serializers import PostSerializer
from posts.models import Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostListAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView): # detail, update, delete
#     permission_classes = [IsAuthorOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

