from rest_framework import serializers
from .models import Author, Book

class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    book_author = AuthorNameSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'book_title', 'book_description', 'book_author', 'book_published_date', 'book_image']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'image', 'books']
