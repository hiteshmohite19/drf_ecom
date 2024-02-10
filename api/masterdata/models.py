from django.db import models
from uuid import uuid4

# Create your models here.


class ColorMasterData(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    color = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["color"]

    def __str__(self):
        return self.color


class SizeMasterData(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    size = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["size"]

    def __str__(self):
        return self.size
