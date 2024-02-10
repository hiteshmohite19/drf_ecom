from rest_framework.serializers import ModelSerializer
from .models import *


class ColorSerializer(ModelSerializer):
    class Meta:
        model = ColorMasterData
        fields = ("color",)


class SizeSerializer(ModelSerializer):
    class Meta:
        model = SizeMasterData
        fields = ("size",)
