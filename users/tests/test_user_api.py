from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

AUTH_TOKEN_URL = reverse('users:login')


class UserTest(APITestCase):
    def setUp(self):
        self.tes_user = User.objects.create_user('test_user', 'test@example.com', 'testpassword')
        self.signup_url = reverse('users:register')

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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        self.assertEqual(response.data['username'], response.data['username'])
        self.assertNotIn('password', response.data)

    def test_toke_creation(self):
        """
        Tests token is being created
        """
        data = {
            "email": "test1@example.com",
            "username": 'test1',
            "password": "test1pass",
        }
        user = User.objects.create_user(**data)

        credentials = {'username': 'test1', 'password': 'test1pass'}

        response = self.client.post(AUTH_TOKEN_URL, credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
