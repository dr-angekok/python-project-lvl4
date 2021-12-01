from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from labels import views
from labels.models import TaskLabel


class LabelTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Igor',
            password='password!@#$123',
        )
        self.client = Client()

    def createLabel(self):
        label = TaskLabel.objects.create(name='Any label')
        return label

    def test_label_create(self):
        label = self.createLabel()
        self.assertTrue(isinstance(label, TaskLabel))
        self.assertEqual(TaskLabel.objects.count(), 1)

    def test_label_view(self):
        self.createLabel()
        request = self.factory.get('/labels/')
        request.user = self.user
        response = views.LabelsView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/login/', {'username': 'Igor', 'password': 'password!@#$123'})
        response = self.client.get('/labels/')
        content = response.content.decode("utf-8")
        self.assertTrue(content.__contains__('Any label'))
