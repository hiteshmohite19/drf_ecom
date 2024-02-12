from django.urls import path, include
from rest_framework import routers
from .views import CategoryDetails

urlpatterns = [
    path("", CategoryDetails.as_view({"get": "get"})),
    path("<name>/", CategoryDetails.as_view({"get": "get_by_category"})),
]
