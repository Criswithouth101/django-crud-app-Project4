from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    path("books/add/", views.BookCreateView.as_view(), name="add"),
    path("books/<int:pk>/edit/", views.BookUpdateView.as_view(), name="edit"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="delete"),

]
