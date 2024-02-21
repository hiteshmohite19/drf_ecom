from django.contrib import admin
from .models import Products, ProductImages

# Register your models here.

admin.site.register(Products)
admin.site.register(ProductImages)


class ProductImagesAdmin(admin.ModelAdmin):
    ordering = ("-created",)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name",)


# class ProductsAdmin(admin.ModelAdmin):
#     list_display = ("color", "size", "quantity")
