from msilib.schema import ListView

from django.core.cache import cache
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializer import PostSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @method_decorator(cache_page(30))
    def get(self,  *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_queryset(self):
        queryset = Post.objects.all().objects.select_related('author').prefetch_related('tags')


class PostDetailView(APIView):

    def get (self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        cache_key = f'post:{post_id}'
        post=cache.get(cache_key)
        if post is None:
            post = Post.objects.raw('select * from post_post;')
            serializer = PostSerializer(post)
            cache.set(cache_key, serializer.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return post








