from django.urls import path
from .views import *

urlpatterns = [
    path("colors", Colors.as_view()), 
    path("size", Size.as_view())
]
