from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from olcha.models import Category, Group, Product


class CategoryImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField('get_url')

    def get_url(self, obj):
        return obj.category_imageimage.url

    class Meta:
        model = Category
        fields = ['id', 'url']


class CategoryModelSerializer(ModelSerializer):
    image = CategoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
