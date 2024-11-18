# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

@api_view(['GET', 'POST'])  # Allow both GET and POST
def login(request):
    if request.method == 'GET':
        # Handle GET request: return all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Handle POST request: create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created successfully
        return Response(serializer.errors, status=400)  # Bad request if validation fails
