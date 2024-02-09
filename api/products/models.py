from django.db import models
from uuid import uuid4
from django.utils.text import slugify

# Create your models here.


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True)
    descriptions = models.TextField()

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()


class ProductVariations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{str(self.color)} {str(self.size)} {str(self.quantity)}"


class ProductImages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="products/")
    variants = models.ForeignKey(ProductVariations, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.image

    def save(self):
        for field in self._meta.fields:
            if field.name == "image":
                field.upload_to = f"products/{self.product}/"
        super().save()
