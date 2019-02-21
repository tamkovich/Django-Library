from django.test import TestCase

from django.contrib.auth.models import User

from main.models import Book


class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username='tester1',
            first_name='TestName',
            last_name='TestSurname',
            password='test123456789'
        )
        User.objects.create(
            username='trainer',
            first_name='MyName',
            last_name='MySurname',
            password='1234best56789'
        )
        user1 = User.objects.get(id=1)
        user2 = User.objects.get(id=2)
        Book.objects.create(
            title="The Lean StartUp",
            content="super content ... ",
            author="Eric Ries",
            owner=user1,
        )
        Book.objects.create(
            title="Flow: The Psychology of Optimal Experience (Harper Perennial Modern Classics)",
            content="Only one thing!",
            author="Mihaly Csikszentmihalyi",
            owner=user2,
        )

    def test_book_absolute_url(self):
        """Book can return the edit-url via his <id>"""
        book1 = Book.objects.get(id=1)
        book2 = Book.objects.get(id=2)
        self.assertEqual(book1.get_absolute_url(), '/book/1/edit/')
        self.assertEqual(book2.get_absolute_url(), '/book/2/edit/')
