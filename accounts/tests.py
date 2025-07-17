from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):
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