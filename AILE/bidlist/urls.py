# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/bidlist/', views.bidlist),  # For GET and POST
    path('api/bidlist/<int:id>/', views.bidlist_item),  # For DELETE and PATCH by ID
]
