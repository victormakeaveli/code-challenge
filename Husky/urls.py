from django import urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('bank.urls')),
    path('admin/', admin.site.urls),
]
