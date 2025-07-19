from django.test import TestCase

from django.contrib.auth import get_user_model

from django.urls import reverse, resolve

from .views import *

# Create your tests here.
class ModelTests(TestCase):
    # CustomUser Tests
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "testuser@email.com",
            password = "testing321",
        )

        cls.admin_user = get_user_model().objects.create_superuser(
            username = "superuser",
            email = "superuser@email.com",
            password = "testing321",
        )
    
    def test_create_user(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@email.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.username, "superuser")
        self.assertEqual(self.admin_user.email, "superuser@email.com")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)


class ViewTests(TestCase):
    # Sign up tests
    def test_signup_template(self):
        response = self.client.get(reverse("signup"))
        view = resolve("/accounts/signup/")
        form = response.context.get("form")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertContains(response, "Sign Up")
        self.assertNotContains(response, "I should not be here!")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(response, "csrfmiddlewaretoken")