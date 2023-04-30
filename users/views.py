from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer, ProfileSerializer
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class UserView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "수정완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user.user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
