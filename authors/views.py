from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializer import BookSerializer, AuthorSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
@permission_classes([AllowAny])
def all_authors(request):
    paginator           = PageNumberPagination()
    paginator.page_size = 10
    authors             = Author.objects.all()
    result_page         = paginator.paginate_queryset(authors, request)
    serializer          = AuthorSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_author(request) :
    data = request.data 
    try : 
        author = Author.objects.create(
            name = data['name'],
            bio  = data['bio'],
            image = data['image']
        )
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)