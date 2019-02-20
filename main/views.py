from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from main.forms import UserForm


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
            user = form.save()
            form = UserForm()
        args = {
            'users': self.model.objects.all().order_by('-id'),
            'user_form': form,
        }
        return render(request, self.template_name, args)
