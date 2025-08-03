# api/urls.py
from django.urls import path ,include
from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

#create a router and register our viewset with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
router.register(r'comments', CommentViewSet, basename='comment')



urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  #  List view endpoint
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('token/', obtain_auth_token, name='api_token_auth'),  # Token retrieval
]
