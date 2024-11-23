from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Device
from .serializers import DeviceSerializer

@api_view(['GET', 'POST'])
def devicess(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Created successfully
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad request if validation fails

@api_view(['DELETE', 'PATCH'])
def devicess_item(request, id):
    try:
        device = Device.objects.get(id=id)  # Retrieve device by ID
    except Device.DoesNotExist:
        return Response({'error': 'device not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        # Handle DELETE request: delete a device by ID
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # No content to return after deletion

    elif request.method == 'PATCH':
        # Handle PATCH request: partially update a device by ID
        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
