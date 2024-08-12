from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.Serializer) :
    class Meta : 
        model  = Book 
        fields = ['id ', 'book_title' , 'book_description' , 'book_author' , 'book_published_date' , 'book_image']

class AuthorSerializer(serializers.Serializer) : 
    books = BookSerializer(many=True, read_only=True)
    class Meta : 
        model  = Author 
        fields = [ 'id' , 'name' , 'bio' , 'image' , 'books']     