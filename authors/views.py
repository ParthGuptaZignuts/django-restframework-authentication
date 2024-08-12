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
