from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

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

# Create your views here.
