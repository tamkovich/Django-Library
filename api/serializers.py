from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer
)
from django.contrib.auth.models import User

from main.models import Book


class PostCreateSerializer(ModelSerializer):
    owner = CharField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'owner',
            'title',
            'content',
            'author',
        ]
        extra_kwargs = {
            "owner": {
                "read_only": True
            }
        }


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }
