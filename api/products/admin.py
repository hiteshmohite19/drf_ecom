from django.contrib import admin
from .models import Products, ProductVariations, ProductImages

# Register your models here.

admin.site.register(Products)
admin.site.register(ProductVariations)
admin.site.register(ProductImages)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name",)


# class ProductsAdmin(admin.ModelAdmin):
#     list_display = ("color", "size", "quantity")
