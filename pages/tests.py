from django.test import TestCase

from django.test import SimpleTestCase

from django.urls import reverse, resolve

from .views import *

# Create your tests here.
class PagesTests(SimpleTestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse("pages:home"))
        view = resolve("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "Home")
        self.assertNotContains(response, "I should not be on the page.")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_aboutpage_view(self):
        response = self.client.get(reverse("pages:about"))
        view = resolve("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertContains(response, "About")
        self.assertNotContains(response, "I should not be on the page.")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)