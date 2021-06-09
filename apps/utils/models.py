# Django
from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(null=True)
    description = models.TextField(null=True)
    manufacturer = models.CharField(max_length=255, null=True)
    sku = models.CharField(max_length=255, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
