from django.db import models
from uuid import uuid4
from django.contrib import admin

# Create your models here.

class CategoryMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SizeMasterData(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    size = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.size


class SizeVariants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    size = models.ForeignKey(SizeMasterData, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    quantity = models.IntegerField(default=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["size"]

    def __str__(self):
        return f"{str(self.size)}-{str(self.price)}-{str(self.quantity)}"


class ColorMasterData(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    color = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["color"]

    def __str__(self):
        return self.color


class ColorVariants(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    color = models.ForeignKey(ColorMasterData, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    quantity = models.IntegerField(default=10)
    size = models.ManyToManyField(SizeVariants)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["color"]

    @admin.display()
    def get_size_details(self):
        return [s.size for s in self.size.all()]

    def __str__(self) -> ColorMasterData:
        return f"{str(self.color)}-{str(self.price)}-{str(self.quantity)}-{self.get_size_details()}"
