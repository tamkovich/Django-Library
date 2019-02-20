from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author}:{self.title}'
