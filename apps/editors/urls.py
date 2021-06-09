# Django
from django.urls import path

# Views
from .views import main

app_name = 'editors'
urlpatterns = [
    path('', main)
]
