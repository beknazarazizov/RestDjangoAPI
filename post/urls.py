
from django.urls import path

from post.views import PostListView

urlpatterns = [
    path('posts', PostListView.as_view(),name='post_list'),
]