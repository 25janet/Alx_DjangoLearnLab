from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view,
    admin_view,
    librarian_view,
    member_view,

)
 

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Registration using custom view
    path('register/', views.register_view, name='register'),

    # ✅ Login using built-in class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # ✅ Logout using built-in class-based view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
    
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book_view, name='delete_book')
]


