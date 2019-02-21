from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('main:book-edit', kwargs={'id': self.id})

    def get_api_url(self):
        return reverse('api:book-edit', kwargs={'id': self.id})

    def __str__(self):
        return f'{self.author}:{self.title}'
