from bookshelf.models import Book
book = Book.objects.get(title = "nineteen-eightfour")
book.delete()
Book.objects.all()
