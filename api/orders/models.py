from django.db import models
from uuid import uuid4

from api.users.models import User, UserAddress
from api.products.models import Products
from api.masterdata_variants.models import ColorVariants, SizeVariants
from api.masterdata_variants.models import Coupon

# Create your models here.

payment_mode_options = (
    ("cash", "Cash"),
    ("card", "Card"),
    ("upi", "UPI"),
)

payment_status = (
    ("paid", "Paid"),
    ("pending", "Pending"),
)


class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT, null=True)
    payment_mode = models.CharField(null=False, choices=payment_mode_options)
    payment_status = models.CharField(null=False, choices=payment_status)
    transaction_id = models.CharField(null=True)
    order_status = models.CharField(null=True)
    delivery_address = models.ForeignKey(UserAddress, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}-{self.id}"


class OrdersData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    color_variant_id = models.ForeignKey(ColorVariants, on_delete=models.CASCADE)
    size_variant_id = models.ForeignKey(SizeVariants, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_id}-{self.id}"
