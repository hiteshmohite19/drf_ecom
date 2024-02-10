from django.urls import path, include
from .views import ProductDetials


urlpatterns = [
    path("", ProductDetials.as_view({"get": "get"})),
    path("price-filter/", ProductDetials.as_view({"post": "price_filter_data"})),
]
