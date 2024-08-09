from rest_framework import serializers
from .models import Library, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = ['id', 'title', 'author', 'library']

class LibrarySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model  = Library
        fields = ['id', 'name', 'location', 'books']