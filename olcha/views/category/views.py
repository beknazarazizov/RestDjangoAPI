
#
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from olcha.models import Category, Product
from olcha.serializers import CategoryModelSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def retrieve(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateCategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=slug)
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=slug)
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCategoryView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=slug)
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #
    def delete(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

