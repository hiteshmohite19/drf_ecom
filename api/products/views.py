from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from .models import Products, ProductVariations
from .serializers import ProductsSerializer, ProductVariantsSerializer

# Create your views here.


class ProductsList(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductVariantsList(ListCreateAPIView):
    queryset = ProductVariations.objects.all()
    serializer_class = ProductVariantsSerializer


