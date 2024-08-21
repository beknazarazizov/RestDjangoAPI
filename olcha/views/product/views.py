from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from olcha import permissions
from olcha.permissions import IsOwnerIsAuthenticated
from olcha.models import Product
from olcha.serializers import ProductSerializer, ProductDetailSerializer, AttributeSerializer, LoginSerializer, \
    RegisterSerializer


# class ProductListView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)

class ProductListView(generics.ListCreateAPIView):

    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        group_slug = self.kwargs.get('group_slug')

        queryset = Product.objects.select_related('group__category')

        if category_slug and group_slug:
            queryset = queryset.filter(group__category__slug=category_slug, group__slug=group_slug)
        elif category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        elif group_slug:
            queryset = queryset.filter(group__slug=group_slug)

        return queryset



# class ProductDetailView(APIView):
#     def get_object(self, slug):
#         product = Product.objects.get(slug=slug)
#         serializer = ProductSerializer(product,many=False)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)


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


# class ProductDeleteView(APIView):
#
#     def delete(self, request, slug):
#         product = Product.objects.get(slug=slug)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

class ProductDetail(APIView):
    permission_classes = IsOwnerIsAuthenticated
    def get(self, request, category_slug, group_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, category_slug, group_slug, product_slug):
        product = Product.objects.get(slug=product_slug)
        serializer = ProductDetailSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_slug, group_slug, product_slug):
        product = Product.objects.get(slug=product_slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductsAttribute(APIView):
#     def get(self, request, category_slug, group_slug):
#         products = Product.objects.filter(group__category__slug=category_slug, group__slug=group_slug)
#         serializer = AttributeSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ProductAttribute(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('group').prefetch_related('attributes__key', 'attributes__value')

    serializer_class = AttributeSerializer
    lookup_field = 'slug'


# class ProductAttribute(APIView):
#
#     def get(self, request, category_slug, group_slug, product_slug):
#         product = Product.objects.get(slug=product_slug)
#         serializer = AttributeSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, category_slug, group_slug, product_slug):
#         product = Product.objects.get(slug=product_slug)
#         serializer = AttributeSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, category_slug, group_slug, product_slug):
#         product = Product.objects.get(slug=product_slug)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "username": {
                    "about": "Not Exist"
                }
            }
            if User.objects.filter(username=request.data['username']).exists():
                user = User.objects.get(username=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
        except Token.DoesNotExist:
            return Response({"error": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "user": RegisterSerializer(user).data,
                "token": token.key,
                "message": "User created successfully."
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
