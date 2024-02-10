from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

# Create your views here.

class Colors(ListAPIView):
    queryset = ColorMasterData.objects.all()
    serializer_class = ColorSerializer


class Size(ListAPIView):
    queryset = SizeMasterData.objects.all()
    serializer_class = SizeSerializer
