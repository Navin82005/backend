from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    StaffLoginSerializer,
    get_tokens_for_user,
    StudentLoginSerializer,
)
from django.contrib.auth import authenticate
from .models import *


# ACCESS TOKEN REFRESHER API
class RefreshAccessToken(APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data["refresh_token"]

        return Response(
            {
                "message": "Token obtained successfully",
                "access_token": refresh_token.access_token,
            },
            status=status.HTTP_200_OK,
        )


# LOGIN API
class StaffLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Serialize and validate the incoming data
        serializer = StaffLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            # Authenticate the user
            user = Staff.authenticate(username, password)

            if user is not None:
                # User is authenticated
                tokens = get_tokens_for_user(user)

                return Response(
                    {
                        "tokens": tokens,
                        "userData": user.get_main_data(),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                # Invalid credentials
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            # Invalid data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Serialize and validate the incoming data
        serializer = StaffLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            # Authenticate the user
            user = authenticate(username=username, password=password)

            if user is not None:
                # User is authenticated
                tokens = get_tokens_for_user(user)

                return Response(
                    tokens,
                    status=status.HTTP_200_OK,
                )
            else:
                # Invalid credentials
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            # Invalid data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Serialize and validate the incoming data
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            # Authenticate the user
            user = Student.authenticate(username, password)

            if user is not None:
                # User is authenticated
                tokens = get_tokens_for_user(user)

                return Response(
                    {
                        "tokens": tokens,
                        "userData": user.get_main_data(),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                # Invalid credentials
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            # Invalid data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
