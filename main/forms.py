from django import forms
from django.contrib.auth.models import User

from main.models import Book


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class BookCreateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write about it...'
            }
        )
    )

    class Meta:
        model = Book
        fields = ('title', 'content', 'author')

    def save(self, user):
        book = super(BookCreateForm, self).save(commit=False)
        book.owner = user
        book.save()

        return book
