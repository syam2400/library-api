from django.shortcuts import render
from rest_framework import viewsets
from library.models import Book
from rest_framework import serializers
from library.serializer import BookSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


class BookViewSet(viewsets.ModelViewSet):
    # permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
