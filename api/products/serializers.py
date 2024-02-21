from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Products, ProductImages
from api.masterdata_variants.serializers import *


class ProductsImagesSerializer(ModelSerializer):

    class Meta:
        model = ProductImages
        fields = "__all__"


class ProductsSerializer(ModelSerializer):
    color = ColorVariantSerializer(many=True)
    product_images = ProductsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = "__all__"
