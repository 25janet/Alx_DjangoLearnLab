from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path('books/', book_list, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
