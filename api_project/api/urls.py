# api/urls.py
from django.urls import path
from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
#create a router and register our viewset with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  #  List view endpoint
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
