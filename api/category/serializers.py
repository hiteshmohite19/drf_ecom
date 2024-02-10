from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Category
from api.products.serializers import ProductsSerializer


class CategorySerializer(ModelSerializer):
    products = ProductsSerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"