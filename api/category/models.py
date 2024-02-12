from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from api.products.models import Products
from api.masterdata_variants.models import CategoryMaster

# Create your models here.


class Category(models.Model):
    category = models.ForeignKey(CategoryMaster, on_delete=models.PROTECT, default=None)
    slug = models.SlugField(max_length=150, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return str(self.category)

    def save(self):
        self.slug = slugify(str(self.category))
        super().save()
