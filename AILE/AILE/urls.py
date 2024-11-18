# AILE/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('log.urls')),
    path('', include('bidlist.urls')),
    path('', include('shipment.urls')),
]
