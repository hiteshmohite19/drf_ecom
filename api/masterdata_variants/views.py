from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.core.cache import cache
from .models import *
from .serializers import *

# Create your views here.


class Colors(ViewSet):

    def get(self, request):
        return Response(cache.get('colors'))


class Size(ViewSet):
    
    def get(self,request):
        return Response(cache.get('size'))
