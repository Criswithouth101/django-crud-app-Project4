from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'content', 'book']
        read_only_fields = ['id', 'user', 'book']

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'owner', 'reviews']
