from django import forms
from django.contrib.auth.models import User

from main.models import Book


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class ArticleForm(forms.ModelForm):
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
        fields = ('title', 'content',)

    def save(self, user, category):
        article = super(ArticleForm, self).save(commit=False)
        article.author = user
        # article.slug = slugify(article.title)
        article.category = category
        article.save()

        return article
