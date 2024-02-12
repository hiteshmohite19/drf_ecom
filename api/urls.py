from django.urls import path, include

urlpatterns = [
    path("products/", include("api.products.urls")),
    path("categories/", include("api.category.urls")),
    path("variants/", include("api.masterdata_variants.urls")),
]
