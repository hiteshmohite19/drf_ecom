from django.urls import path, include
from rest_framework import routers
from .views import CategoryDetails

urlpatterns = [
    path("", CategoryDetails.as_view({"get": "get"})),
    path("count", CategoryDetails.as_view({"get": "category_count"})),
    path("<name>/", CategoryDetails.as_view({"get": "get_by_category"})),
]
