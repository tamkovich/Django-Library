from django.urls import path, re_path

from main.views import UserListView, UserBookLibView, BookEditView

app_name = 'main'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    re_path('^lib/(?P<id>\d+)/$', UserBookLibView.as_view(), name='user-lib'),
    re_path('^book/(?P<id>\d+)/edit/$', BookEditView.as_view(), name='book-edit'),
]
