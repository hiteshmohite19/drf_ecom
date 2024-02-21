from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Products
from .serializers import ProductsSerializer, ProductsImagesSerializer

# Create your views here.


class ProductDetials(ViewSet):

    def products(self, request):
        filter = request.data
        # {"color__color__color":"Green"}
        queryset = Products.objects.filter(**filter)
        serializer = ProductsSerializer(queryset, many=True)
        products = serializer.data

        return Response(products)

    def product_details(self, request, slug):
        product = Products.objects.get(slug=slug)
        serializer = ProductsSerializer(product)
        product = serializer.data

        response = {
            "name": product["name"],
            "descriptions": product["descriptions"],
            "price": product["price"]
        }

        variants = {}
        
        for colors in product["color"]:

            size_data = {}
            for size in colors["size"]:
                size_data[size["size"]["size"]] = {
                    "size_price": size["price"],
                    "size_quantity": size["quantity"],
                }

            variants[colors["color"]["color"]] = {
                "color_quantity": colors["quantity"],
                "color_price": colors["price"],
                "size": size_data,
            }

            response['size']=set(size_data.keys())

        response["colors"]= set(variants.keys())
        response["variants"]= variants,

        return Response(response)
