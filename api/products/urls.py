from django.urls import path, include

from .views import ProductsList,ProductVariantsList

urlpatterns = [
    path("", ProductsList.as_view()),
    path("product-variants/", ProductVariantsList.as_view()),
]
