# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user.models import User
from user.serializers import UserSerializer
from device.models import Device
from device.serializers import DeviceSerializer
from product.models import Product
from product.serializers import ProductSerializer


# ============== TRACK ME ============

@api_view(['POST'])
def track_me(request):
    user_id=request.data.get('user_id')
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "user_id not found"}, status=status.HTTP_404_NOT_FOUND)
    
    device_id=request.data.get('device_id')
    try:
        device = Device.objects.get(id=device_id)
        device_serializer = DeviceSerializer(device, data=request.data, partial=True)
        if device_serializer.is_valid():
            device_serializer.save()
        if(int(device_serializer.data["product_id"])>0):
            product = Product.objects.get(id=device_serializer.data["product_id"])
            product_serializer = ProductSerializer(product, data=request.data, partial=True)
            if product_serializer.is_valid():
                product_serializer.save()
            connected_product=product_serializer.data
        else:
            connected_product="Not Connected"

        
        if user.role == 'customer':
            user_serializer = UserSerializer(user, data={"role":"seller"}, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"Device":device_serializer.data,"Product":connected_product},status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"message": "Already A Seller"}, status=status.HTTP_200_OK)
        
    except Device.DoesNotExist:
        return Response({"error": "device_id not found"}, status=status.HTTP_404_NOT_FOUND)

    