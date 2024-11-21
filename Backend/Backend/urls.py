from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('routes/', include('openroute.urls')),
    path('api/', include('user.urls')),  
    path('api/', include('product.urls')),  
    path('api/', include('bids.urls')),  
    path('api/', include('drivers.urls')),  
    path('api/', include('routes.urls')),  
]
