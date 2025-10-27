from django.urls import path
from .api_views import BookListCreateView, BookDetailView, ReviewCreateView, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:book_pk>/reviews/', ReviewCreateView.as_view(), name='review_create'),
]
