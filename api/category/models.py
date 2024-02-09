from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from products.models import Products
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Products)

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()
