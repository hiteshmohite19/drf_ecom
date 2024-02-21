from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategoryDetailsSerializer

# Create your views here.


class CategoryDetails(ViewSet):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategoryDetailsSerializer(category, many=True)
        return Response(serializer.data)

    def category_count(self, request):
        category = Category.objects.all()
        serializer = CategoryDetailsSerializer(category, many=True)
        categories = serializer.data

        response = []

        for category in categories:
            resp = {
                "category": category["category"]["name"],
                "count": len(category["products"]),
            }
            response.append(resp)

        return Response(response)

    def get_by_category(self, request, name):
        category = Category.objects.filter(slug=name)
        serializer = CategoryDetailsSerializer(category, many=True)
        return Response(serializer.data)
