from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book, Review


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books" 

    def get_queryset(self):
        return Book.objects.select_related("owner").order_by("-published_date")

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date', 'price']
    success_url = reverse_lazy('books:index')
    template_name = "books/book_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookOwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class BookUpdateView(LoginRequiredMixin, BookOwnerRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'published_date', 'price']
    template_name = "books/book_form.html"

class BookDeleteView(LoginRequiredMixin, BookOwnerRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("books:index")


class ReviewOwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'content']
    template_name = "books/review_form.html"

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        form.instance.book = book
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        return context

    def get_success_url(self):
        return self.object.book.get_absolute_url()


class ReviewUpdateView(LoginRequiredMixin, ReviewOwnerRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'content']
    template_name = "books/review_form.html"

    def get_success_url(self):
        return self.object.book.get_absolute_url()

class ReviewDeleteView(LoginRequiredMixin, ReviewOwnerRequiredMixin, DeleteView):
    model = Review
    template_name = "books/review_confirm_delete.html"

    def get_success_url(self):
        return self.object.book.get_absolute_url()
    
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


