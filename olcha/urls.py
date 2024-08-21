from django.contrib import admin
from django.urls import path, include

from olcha.views.category.views import CategoryListView, CategoryDetail,CreateCategoryView,UpdateCategoryView,DeleteCategoryView
from olcha.views.group.views import GroupApiView, GroupCreateApiView, GroupUpdateApiView, GroupDeleteApiView, \
    GroupDetailApiView
from olcha.views.product.views import ProductListView, ProductDetail, ProductAttribute, ProductAttribute, RegisterView, \
    LoginView, LogOutView

urlpatterns = [
    path('category_list/',CategoryListView.as_view(),name='category_list'),
    path('category/<slug:slug>/detail/',CategoryDetail.as_view(),name='category_detail'),
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
    path('categories/<slug:category_slug>/<slug:group_slug>/', ProductListView.as_view()),
    path('categories/<slug:category_slug>/<slug:group_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('categories/<slug:category_slug>/<slug:group_slug>/<slug:product_slug>/attribute/',
         ProductAttribute.as_view()),
    path('categories/<slug:category_slug>/<slug:group_slug>/products/attributes/', ProductAttribute.as_view()),
    #Register
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogOutView.as_view()),


]