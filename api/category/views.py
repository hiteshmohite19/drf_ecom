from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products
from .models import Category
from .serializers import CategorySerializer

# Create your views here.


class CategoryDetails(APIView):

    response = {}

    def get(self, request):
        category = Category.objects.all()
        # self.response["category"] = CategorySerializer(category, many=True)
        # category = CategorySerializer(category, many=True)
        print(category)
        return Response(category.data)
