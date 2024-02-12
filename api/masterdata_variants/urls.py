from django.urls import path
from .views import *

urlpatterns = [
    path("colors/", Colors.as_view({'get':'get'})), 
    path("size/", Size.as_view())
]
