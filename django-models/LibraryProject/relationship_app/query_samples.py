import os
import django

# SETUP DJANGO ENVIRONMENT
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author_name = "John Doe"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

    # 2. List all books in a specific library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()  # This uses related_name='books'
        print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

    # 3. Retrieve the librarian for a specific library
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # This uses related_name='librarian'
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'")

if __name__ == '__main__':
    run_queries()
