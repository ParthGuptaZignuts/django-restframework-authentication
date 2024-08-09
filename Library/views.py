from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Library, Book
from .Serializer import LibrarySerializer, BookSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
@permission_classes([AllowAny]) 
def all_libraries(request):
    paginator           = PageNumberPagination()
    paginator.page_size = 10
    libraries           = Library.objects.all()
    result_page         = paginator.paginate_queryset(libraries, request)
    serializer          = LibrarySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def single_library(request, library_id):
    try:
        library    = Library.objects.get(id=library_id)
        serializer = LibrarySerializer(library)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Library not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny]) 
def create_library(request):
    data = request.data
    try:
        library  = Library.objects.create(
        name     = data['name'],
        location = data['location']
        )
        serializer = LibrarySerializer(library)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny]) 
def update_library(request, library_id):
    data = request.data
    try:
        library           = Library.objects.get(id=library_id)
        library.name      = data['name']
        library.location  = data['location']
        library.save()
        serializer = LibrarySerializer(library)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Library not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([AllowAny]) 
def delete_library(request, library_id):
    try:
        library = Library.objects.get(id=library_id)
        library.delete()
        return Response({'message': 'Library deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return Response({'error': 'Library not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def all_books(request):
    paginator           = PageNumberPagination()
    paginator.page_size = 10
    books               = Book.objects.all()
    result_page         = paginator.paginate_queryset(books, request)
    serializer          = BookSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def single_book(request, book_id):
    try:
        book       = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny]) 
def create_book(request):
    data = request.data
    try:
        book       = Book.objects.create(
        title      = data['title'],
        author     = data['author'],
        library_id = data['library']
        )
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny]) 
def update_book(request, book_id):
    data = request.data
    try:
        book            = Book.objects.get(id=book_id)
        book.title      = data['title']
        book.author     = data['author']
        book.library_id = data['library']
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([AllowAny]) 
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
