from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Products
from .serializers import ProductsSerializer

# Create your views here.


class ProductDetials(ViewSet):

    def get(self, request):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)

    # def filter_data(self, request):
    #     data = request.data
    #     products = Products.objects.filter(**data)
    #     serializer = ProductsSerializer(products, many=True)
    #     return Response(serializer.data)

