from rest_framework.serializers import ModelSerializer
from .models import Products
from api.masterdata_variants.serializers import *


class ProductsSerializer(ModelSerializer):
    color = ColorVariantSerializer(many=True)

    class Meta:
        model = Products
        fields = "__all__"
