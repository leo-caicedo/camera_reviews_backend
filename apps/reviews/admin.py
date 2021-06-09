# Django
from django.contrib import admin

# Models
from .models import Review, Camera

admin.site.register(Review)
admin.site.register(Camera)
