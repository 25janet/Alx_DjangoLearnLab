from django.shortcuts import render
from rest_framework import generics, status,filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from datetime import date
from django_filters.rest_framework import DjangoFilterBackend

# List all books - anyone can view
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Enable filtering + searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    # Ordering
    ordering_fields = ['title', 'publication_year']  # fields users can sort by
    ordering = ['publication_year']  


# Retrieve a single book - anyone can view
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a book - only authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pub_year = serializer.validated_data.get("publication_year")
        if pub_year > date.today().year:
            raise ValueError("Publication year cannot be in the future.")
        serializer.save()

# Update a book - only authenticated users
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

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

# Delete a book - only authenticated users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
