from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    query_set = User.objects.all
    serializer_class = RegisterSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data["id"])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": response.data
        }, status=status.HTTP_201_CREATED)

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        token = Token.objects.get(key=response.data['token'])
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(id=token.user_id)
        return Response({
            "token": token.key,
            "user": UserSerializer(user).data
        })
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user