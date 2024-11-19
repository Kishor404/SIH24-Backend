from django.urls import path
from .views import log,log_item

urlpatterns = [
    path('users/', log, name='user-list-create'),
    path('users/<int:pk>/', log_item, name='user-detail'),
]
