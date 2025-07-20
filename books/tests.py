from django.test import TestCase

from django.urls import reverse

from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Harry Potter",
            author = "JK Rowling",
            price = "25.00",
        )

    def test_book_model(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.author, "JK Rowling")
        self.assertEqual(self.book.price, "25.00")

    def test_book_list_view(self):
        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_list.html")
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, self.book.title)

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "books/book_detail.html")
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book.author)
        self.assertContains(response, self.book.price)
