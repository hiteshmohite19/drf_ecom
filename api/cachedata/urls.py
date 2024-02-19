from django.urls import path, include
from .views import CacheData


urlpatterns = [
    # path("categories-count/", CacheData.as_view({"get": "categories_count"})),
]
