from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from olcha.models import Product
from olcha.serializers import ProductSerializer


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get_object(self, slug):
        product = Product.objects.get(slug=slug)
        serializer = ProductSerializer(product,many=False)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    def put(self, request, slug):
        product = Product.objects.get(slug=slug)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):
    def delete(self, request, slug):
        product = Product.objects.get(slug=slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




