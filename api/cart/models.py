from django.db import models
from uuid import uuid4

from api.users.models import User
from api.products.models import Products
from api.masterdata_variants.models import ColorVariants, SizeVariants

# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    color_variant_id = models.ForeignKey(ColorVariants, on_delete=models.CASCADE)
    size_variant_id = models.ForeignKey(SizeVariants, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


