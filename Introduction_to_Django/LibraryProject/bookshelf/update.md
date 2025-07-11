from bookshelf.models import Book
book = Book.objects.get(title = "1984")
book.title = "nineteen-eightfour"
book.save()
print(book.title)
