from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, filters, viewsets
from django.shortcuts import get_object_or_404
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class BookListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        self.check_object_permissions(request, book)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        self.check_object_permissions(request, book)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        serializer = ReviewSerializer(data=request.data)
        print("REVIEW DATA:", request.data)
        if serializer.is_valid():
            serializer.save(book=book, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'description']

