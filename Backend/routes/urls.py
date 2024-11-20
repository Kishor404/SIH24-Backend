from django.urls import path
from .views import routess,routess_item

urlpatterns = [
    path('routes/', routess, name='routes-list-create'),
    path('routes/<int:pk>/', routess_item, name='routes-detail'),
]
