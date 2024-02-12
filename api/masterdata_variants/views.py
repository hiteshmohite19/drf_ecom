from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import *
from .serializers import *

# Create your views here.


class Colors(ViewSet):

    def get(self, request):
        colors = ColorVariants.objects.all()
        serializer = ColorVariantSerializer(colors, many=True)
        return Response(serializer.data)


class Size(ListAPIView):
    queryset = SizeVariants.objects.all()
    serializer_class = SizeVariantSerializer
