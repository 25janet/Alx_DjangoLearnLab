from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permisssions import IsAuthenticated, IsAdminUser
from .permissions import IsVerifiedUser


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#create a viewset for book model
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsVerifiedUser]
class CommentViewSet(viewsets.ModelViewSet):
    """
    Only authenticated users can list/retrieve.
    Only admins can create/update/delete.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # Combine built-in and custom:
    permission_classes = [IsAuthenticated, IsAdminUser]

# Create your views here.
