from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    author = serializers.CharField(max_length=20)
    isbn = serializers.CharField(max_length=50)
    publisher = serializers.CharField(max_length=50)

    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'