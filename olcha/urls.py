from django.contrib import admin
from django.urls import path, include

from olcha.views import CategoryView

urlpatterns = [
    path('category_list/',CategoryView.as_view(),name='category_list'),

]