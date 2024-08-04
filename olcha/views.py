from urllib import response

from django.shortcuts import render
from rest_framework import status, response
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from olcha.models import Category


# Create your views here.

class CategoryView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        categories = Category.objects.all()
        category_list = [
            {'category_title': category.category_title,
             'category_image': request.build_absolute_uri(category.category_image.url),
             }
            for category in categories]
        return Response(data=category_list)

