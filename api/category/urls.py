from django.urls import path, include
from rest_framework import routers
from .views import CategoryDetails

urlpatterns = [
    path("", CategoryDetails.as_view({"get": "get"})),
    path("", CategoryDetails.as_view({"post": "filtered_data"})),
    path("<name>/", CategoryDetails.as_view({"get": "get_by_category"})),
]
