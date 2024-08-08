from django.contrib import admin
from django.urls import path, include

from olcha.views.category.views import CategoryListView, CategoryDetail,CreateCategoryView,UpdateCategoryView,DeleteCategoryView
from olcha.views.group.views import GroupApiView, GroupCreateApiView, GroupUpdateApiView, GroupDeleteApiView, \
    GroupDetailApiView

urlpatterns = [
    path('category_list/',CategoryListView.as_view(),name='category_list'),
    path('category/<slug:slug>detail/',CategoryDetail.as_view(),name='category_detail'),
    path('category_create/',CreateCategoryView.as_view(),name='category_create'),
    path('category<slug:slug>/update /', UpdateCategoryView.as_view(),name='category_update'),
    path('category/<slug:slug>/delete/', DeleteCategoryView.as_view(), name='category_delete'),

    #group
    path('groups/',GroupApiView.as_view(),name='groups'),
    path('group/create/',GroupCreateApiView.as_view(),name='group/create'),
    path('group/<int:pk>/update/',GroupUpdateApiView.as_view(),name='group/update'),
    path('group/<int:pk>/delete/',GroupDeleteApiView.as_view(),name='group/delete'),
    path('group/<int:pk>/detail/',GroupDetailApiView.as_view(),name='group/detail'),
    #product


]