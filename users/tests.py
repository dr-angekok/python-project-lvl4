from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase


class UserTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Igor',
            password='password!@#$123',
        )
        self.client = Client()

    def test_create_user(self):
        client = Client()
        response = client.post('/login/', {'username': 'Igor', 'password': 'password!@#$123'})
        self.assertEqual(response.status_code, 302)
        response = client.get('/users/')
        content = response.content.decode("utf-8")
        self.assertTrue(content.__contains__('Igor'))
