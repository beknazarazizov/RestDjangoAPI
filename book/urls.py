from django.contrib import admin
from django.urls import path, include

from book.views import BookListPpiView

urlpatterns = [
    path('book_list/',BookListPpiView.as_view(),name='books'),
]