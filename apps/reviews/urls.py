# Django
from django.urls import path

# Views
from .views import main

app_name = 'reviews'
urlpatterns = [
    path('', main)
]
