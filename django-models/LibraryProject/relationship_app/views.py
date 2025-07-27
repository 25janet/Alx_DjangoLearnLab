from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def book_list(request):
    book = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/book_list.html', {'book' : book})
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Create your views here.
