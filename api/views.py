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
    PostCreateSerializer,
    UserListSerializer
)


class UserListAPIView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # @staticmethod
    # def _get_object(id):
    #     try:
    #         return User.objects.get(pk=id)
    #     except User.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, format=None):
    #     users = User.objects.all()
    #     serializer = UserListSerializer(users, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     return redirect(reverse('api:user-list'))
