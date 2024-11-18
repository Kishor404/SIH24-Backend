# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/shipment/', views.Shipment),  # For GET and POST
    path('api/shipment/<int:id>/', views.Shipment_item),  # For DELETE and PATCH by ID
]
