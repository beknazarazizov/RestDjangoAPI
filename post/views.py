from msilib.schema import ListView

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from post.models import Post
from post.serializer import PostSerializer

#
# Create your views here.
class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer








