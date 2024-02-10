from rest_framework.serializers import ModelSerializer
from .models import Products, ProductVariations


class ProductVariantsSerializer(ModelSerializer):
    class Meta:
        model = ProductVariations
        fields = ("size", "color", "quantity", "price")


class ProductsSerializer(ModelSerializer):
    variations = ProductVariantsSerializer(many=True)

    class Meta:
        model = Products
        fields = "__all__"
