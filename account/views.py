from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from account.renderers import UserRenderer

from account.serializers import UserLoginSerializer, UserRegistrationSerializer


class UserRegistrationView(APIView):

    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)  
            if user is not None:
                return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"errors": {'non_field_errors': ['Invalid email or password']}}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)