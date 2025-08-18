from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book
class BookAPITestCase(APITestCase):

    def setUp(self):
        # Test client
        self.client = APIClient()

        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create test books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)

        # URLs
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.pk})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.pk})

    # ---------------------- READ TESTS ----------------------
    def test_list_books(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Anyone can view book detail"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    # ---------------------- CREATE TESTS ----------------------
    def test_create_book_unauthenticated(self):
        """Unauthenticated users should be forbidden from creating"""
        data = {"title": "New Book", "author": "Author C", "publication_year": 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "author": "Author C", "publication_year": 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_with_future_year(self):
        """Reject creating a book with a future publication year"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Future Book", "author": "Author D", "publication_year": 3000}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ---------------------- UPDATE TESTS ----------------------
    def test_update_book_unauthenticated(self):
        """Unauthenticated users should be forbidden from updating"""
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2020}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Authenticated users can update book details"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2020}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_future_year(self):
        """Reject updating a book with a future year"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Bad Update", "author": "Author A", "publication_year": 4000}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ---------------------- DELETE TESTS ----------------------
    def test_delete_book_unauthenticated(self):
        """Unauthenticated users cannot delete"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------------------- FILTER / SEARCH / ORDER ----------------------
    def test_filter_books_by_publication_year(self):
        """Filter books by year"""
        response = self.client.get(f"{self.list_url}?publication_year=2021")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    def test_search_books_by_title(self):
        """Search books by title"""
        response = self.client.get(f"{self.list_url}?search=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_order_books_by_title(self):
        """Order books alphabetically by title"""
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))