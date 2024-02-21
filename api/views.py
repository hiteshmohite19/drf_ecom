from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Create your views here.


class ApiList(ViewSet):

    def get(self, request):

        api_list = [
            {
                "name": "Category Products count",
                "api": "http://localhost:8000/api/categories/categories_count/",
                "method": "get",
                "description": "This api will return Categories and count of products in that category",
            },
            {
                "name": "Products",
                "api": "http://localhost:8000/api/products/",
                "method": "post",
                "description": "This api will return all the products available, if filter is applied then it will return products accordingly",
            },
            {
                "name": "Products",
                "api": "http://localhost:8000/api/products/",
                "method": "post",
                "payload": {"color__color__color": "Green"},
                "description": "This api will return all the products available, if filter is applied then it will return products accordingly",
            },
            {
                "name": "Products details",
                "api": "http://localhost:8000/api/products/product-details/samsung-m51",
                "method": "get",
                "description": "Product details will be returned based on slug",
            },
            {
                "name": "Color and count",
                "api": "http://localhost:8000/api/colors-count/",
                "method": "post",
                "description": "This api will return all the colors available and count of products available for that color",
            },
        ]

        return Response(api_list)
