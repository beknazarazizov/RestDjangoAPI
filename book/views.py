from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book


# Create your views here.


class BookListPpiView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        book = Book.objects.all()
        books = [book.title for book in book]
        return Response(data=books, status=status.HTTP_200_OK)
