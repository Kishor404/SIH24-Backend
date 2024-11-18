# log/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.login),  # Single endpoint for both GET and POST
]
