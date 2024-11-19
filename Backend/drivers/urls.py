from django.urls import path
from .views import driverr,driverr_item

urlpatterns = [
    path('drivers/', driverr, name='driver-list-create'),
    path('drivers/<int:pk>/', driverr_item, name='driver-detail'),
]
