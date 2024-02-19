from django.urls import path, include
from .views import ProductDetials


urlpatterns = [
    path("", ProductDetials.as_view({"post": "get"})),
    # path("price-filter/", ProductDetials.as_view({"post": "filter_data"})),
]
