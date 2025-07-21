from django.test import TestCase

from django.urls import reverse

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .models import Book, Review

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Harry Potter",
            author = "JK Rowling",
            price = "25.00",
        )

        cls.special_permission = Permission.objects.get(
            codename="special_status"
        )

        cls.user = get_user_model().objects.create_user(
            username = "reviewuser",
            email = "reviewuser@email.com",
            password = "testing321",
        )

        cls.review = Review.objects.create(
            book = cls.book,
            author = cls.user,
            review = "An excellent review",
        )

    def test_book_model(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.author, "JK Rowling")
        self.assertEqual(self.book.price, "25.00")

    def test_book_list_view_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="testing321")
        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_list.html")
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, self.book.title)

    def test_book_list_view_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "%s?next=/books/" % (reverse("account_login"))
        )
        response = self.client.get(
            "%s?next=/books/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_book_detail_view(self):
        self.client.login(email="reviewuser@email.com", password="testing321")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "books/book_detail.html")
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "An excellent review")
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book.author)
        self.assertContains(response, self.book.price)
        self.assertContains(response, self.review.review)
