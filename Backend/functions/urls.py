from django.urls import path
from .views import track_me

urlpatterns = [
    path('trackme/', track_me, name='track_me')
]
