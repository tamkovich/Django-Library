from django.urls import path

from main.views import UserListView

app_name = 'main'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
]
