from django.urls import path, include
from .views import ProductDetials


urlpatterns = [
    path("", ProductDetials.as_view({"post": "products"})),
    path(
        "product-details/<str:slug>", ProductDetials.as_view({"get": "product_details"})
    ),
]
