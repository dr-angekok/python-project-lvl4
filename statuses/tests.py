from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from statuses import views
from statuses.models import TaskStatus


class SratusTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Igor',
            password='password!@#$123',
        )
        self.client = Client()

    def createStatus(self):
        status = TaskStatus.objects.create(name='Any status')
        return status

    def test_status_create(self):
        status = self.createStatus()
        self.assertTrue(isinstance(status, TaskStatus))
        self.assertEqual(TaskStatus.objects.count(), 1)

    def test_status_view(self):
        self.createStatus()
        request = self.factory.get('/statuses/')
        request.user = self.user
        response = views.StatusesView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/login/', {'username': 'Igor', 'password': 'password!@#$123'})
        response = self.client.get('/statuses/')
        content = response.content.decode("utf-8")
        self.assertTrue(content.__contains__('Any status'))
