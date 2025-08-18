from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions,status
from .models import Book
from serializers import BookSerializer
from datetime import date

class BookListView(generics.ListAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
class BookDetailView(generics.RetrieveAPIView):

    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
class BookCreateview(generics.CreateAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permission.isAuthenticated]

    def perform_create(self,serializer):
        pub_year = serializer.validated_data.get["publication_year"]
        if pub_year > date.today().year:
            raise ValueError("Publication year cannot be in the future.")
        serializer.save()  # Save the book

class BookUpdateView(generics.UpdateAPIView):
    query_set =Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permission.isAuthenticated]
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        
        pub_year = serializer.validated_data.get("publication_year")
        if pub_year and pub_year > date.today().year:
            return Response(
                {"error": "Publication year cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_update(serializer)
        return Response(serializer.data)
class BookDeleteView(generics.DeleteAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permission.isAuthenticated]
