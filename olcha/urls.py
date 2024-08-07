from django.contrib import admin
from django.urls import path, include

from olcha.views import CategoryListView, CategoryDetail,CreateCategoryView,UpdateCategoryView,DeleteCategoryView

urlpatterns = [
    path('category_list/',CategoryListView.as_view(),name='category_list'),
    path('category/<int:id>detail/',CategoryDetail.as_view(),name='category_detail'),
    path('category_create/',CreateCategoryView.as_view(),name='category_create'),
    path('category<slug:slug>/update /' , UpdateCategoryView.as_view(),name='category_create'),
    path('category/<slug:slug>/delete/', DeleteCategoryView.as_view(), name='category-delete'),

]