from django.core.cache import cache
from drf_ecom.settings.base import CACHE_TIMEOUT

from api.cart.models import Cart
from api.category.models import Category
from api.masterdata_variants.models import (
    CategoryMaster,
    SizeMasterData,
    SizeVariants,
    ColorMasterData,
    ColorVariants,
    Coupon,
)
from api.orders.models import Orders, OrdersData
from api.products.models import Products, ProductImages
from api.users.models import User, UserAddress

from api.category.serializers import CategoryDetailsSerializer
from api.masterdata_variants.serializers import ColorSerializer, SizeSerializer

# Create your views here.


class CacheData:

    def categories_count(self):
        categories = Category.objects.all()
        serializer = CategoryDetailsSerializer(categories, many=True)
        categories = serializer.data
        response = []
        for data in categories:
            resp = {
                "id": data["id"],
                "category": data["category"]["name"],
                "products_count": len(data["products"]),
            }
            response.append(resp)
        cache.set("categories-count", response, CACHE_TIMEOUT)

    def colors(self):
        colors = ColorMasterData.objects.all()
        serializer = ColorSerializer(colors, many=True)
        response = []
        for data in serializer.data:
            resp = {
                "id": data["id"],
                "color": data["color"],
            }
            response.append(resp)
        cache.set("colors", response, CACHE_TIMEOUT)

    def size(self):
        size = SizeMasterData.objects.all()
        serializer = SizeSerializer(size, many=True)
        response = []
        for data in serializer.data:
            resp = {
                "id": data["id"],
                "size": data["size"],
            }
            response.append(resp)
        cache.set("size", response, CACHE_TIMEOUT)

    def invoke(self):
        self.categories_count()
        self.colors()
        self.size()
