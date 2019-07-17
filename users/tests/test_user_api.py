from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status


class UserTest(APITestCase):
    def setUp(self):
        self.tes_user = User.objects.create_user('test_user', 'test@example.com', 'testpassword')
        self.signup_url = reverse('register')

    def test_create_user(self):
        """
        Test User is Creating and token is valid
        """

        data = {
            "username": "myuser",
            "email": "myuser@example.com",
            "password": "mypassword"
        }

        response = self.client.post(self.signup_url, data=data)
        self.assertEqual(User.objects.count(), 2)
