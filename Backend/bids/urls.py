from django.urls import path
from .views import Bidd,Bidd_item

urlpatterns = [
    path('bids/', Bidd, name='user-list-create'),
    path('bids/<int:pk>/', Bidd_item, name='user-detail'),
]
