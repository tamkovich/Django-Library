from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from main.forms import UserForm, BookCreateForm
from main.models import Book


class UserListView(TemplateView):

    template_name = 'main/home.html'
    model = User

    def get(self, request, *args, **kwargs):
        args = {
            'users': self.model.objects.all().order_by('-id'),
            'user_form': UserForm(),
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
        args = {
            'users': self.model.objects.all().order_by('-id'),
            'user_form': form,
        }
        return render(request, self.template_name, args)


class UserBookLibView(TemplateView):

    template_name = 'main/library.html'

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs['id'])
        except:
            return Http404
        args = {
            'user': user,
            'books': Book.objects.filter(owner=user),
            'book_form': BookCreateForm(),
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save(user)
            form = BookCreateForm()
        args = {
            'user': user,
            'books': Book.objects.filter(owner=user),
            'book_form': form,
        }
        return render(request, self.template_name, args)


class BookEditView(TemplateView):

    template_name = 'main/book_edit.html'

    def get(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = BookCreateForm(instance=book)
        args = {
            'book_form': form,
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id=kwargs['id'])
        except:
            return Http404
        form = BookCreateForm(request.POST, instance=book)
        if form.is_valid():
            form.save(book.owner)
            return redirect(reverse('main:user-lib', kwargs={'id': book.owner_id}))
        args = {
            'book_form': form
        }
        return render(request, self.template_name, args)
