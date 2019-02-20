from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from main.models import Book
from api.serializers import (
    BookListCreateSerializer,
    UserListCreateSerializer
)


class UserListAPIView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserListCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        users = User.objects.all()
        serializer = UserListCreateSerializer(users, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserBookLibAPIView(ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookListCreateSerializer

    def _get_queryset(self, pk=None):
        if pk:
            return self.queryset.filter(owner_id=pk)
        else:
            return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self._get_queryset(kwargs.get('id')))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, pk=kwargs.get('id'))
        books = Book.objects.filter(owner_id=kwargs.get('id'))
        serializer = BookListCreateSerializer(books, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, pk=None):
        serializer.save(owner_id=pk)
