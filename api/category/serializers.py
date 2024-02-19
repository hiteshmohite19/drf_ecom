from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import *
from api.products.serializers import ProductsSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryMaster
        fields = "__all__"

class CategoryDetailsSerializer(ModelSerializer):
    products = ProductsSerializer(many=True)
    category= CategorySerializer()
    class Meta:
        model = Category
        fields = "__all__"
