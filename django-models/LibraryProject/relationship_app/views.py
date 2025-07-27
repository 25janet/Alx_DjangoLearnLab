from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# ✅ Function-based view: List all books
def list_books(request):
    books = Book.objects.all()  # <-- This line was missing
    return render(request, "relationship_app/list_books.html", {"books": books})  # <-- Template path is correct

# ✅ Class-based view: Show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
