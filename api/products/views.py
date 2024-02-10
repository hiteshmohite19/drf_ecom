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

    def price_filter_data(self, request):
        data = request.data
        filter_query = {"price__lte": data['greater'], "price__gte": data['less']}
        products = Products.objects.filter(**filter_query)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

