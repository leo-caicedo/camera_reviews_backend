# Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.reviews.urls')),
    path('editors', include('apps.editors.urls'))
]
