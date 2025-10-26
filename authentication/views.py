from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
from django.conf import settings
import jwt

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise PermissionDenied(detail='Invalid credentials')

        dt = datetime.now() + timedelta(days=7)
        payload = {
            'sub': str(user.id),  
            'exp': dt
            }


        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        if isinstance(token, bytes):
            token = token.decode('utf-8')

        return Response(
            {
                'token': token,
                'message': f'Welcome back, {user.username}!'
            },
            status=status.HTTP_200_OK
        )

