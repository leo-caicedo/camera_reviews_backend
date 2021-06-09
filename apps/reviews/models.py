# Django
from django.db import models

# Models
from apps.editors.models import Editor

# Utilities
from apps.utils.models import ProductModel


class Camera(ProductModel):
    max_iso = models.IntegerField(null=True)
    type_camera = models.CharField(max_length=30, null=True)
    crop_factor = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    author = models.ForeignKey(Editor, on_delete=models.CASCADE)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
