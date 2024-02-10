from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer

# Create your views here.


class CategoryDetails(ViewSet):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def get_by_category(self, request,name):
        category = Category.objects.filter(slug=name)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
