from rest_framework.serializers import ModelSerializer
from .models import Products, ProductVariations


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductVariantsSerializer(ModelSerializer):
    class Meta:
        model = ProductVariations
        fields = ("size", "color", "quantity", "price", "product")
