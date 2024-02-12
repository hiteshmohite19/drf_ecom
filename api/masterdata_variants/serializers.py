from rest_framework.serializers import ModelSerializer
from .models import *


class SizeSerializer(ModelSerializer):
    class Meta:
        model = SizeMasterData
        fields = "__all__"


class ColorSerializer(ModelSerializer):

    class Meta:
        model = ColorMasterData
        fields = "__all__"


class SizeVariantSerializer(ModelSerializer):
    class Meta:
        model = SizeVariants
        fields = "__all__"


class ColorVariantSerializer(ModelSerializer):
    size = SizeVariantSerializer(many=True)

    class Meta:
        model = ColorVariants
        fields = "__all__"
