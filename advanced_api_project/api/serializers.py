from rest_framework import serializers
from .models import Author,Book
from datetime import date
#book serializer
class BookSerializer(serializers.ModelSerializers):
    class Meta:
        model = Book
        fields = ['title', 'publication_year','author']
    def validate_publication_year(self,value):
        current year = date.today().year
        if value > current_year:
            raise serializers.ValueError("Publication year can not be inthe future.")
        return value
#author serializers
class AuthorSerializer(serializers.ModelSerializers):
    books = BookSerializer(many = True,read_only = True)
    class Meta:
        model = Author
        fields = ['name', 'books']
        