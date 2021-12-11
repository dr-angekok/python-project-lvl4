from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from . import views
from .models import TaskLabel

TEST_CASE = (
    (('/labels/', '/login/',
      {'username': 'Igor', 'password': 'password!@#$123'}), ('Any label',)),
    (('/labels/1/', None,
      None), ('Any label')),
    (('/labels/', '/labels/1/update/',
      {'name': 'Changed label', }), ('Changed label', '"success">Метка успешно изменена<')),
    (('/labels/', '/labels/1/delete/',
      None), ('"success">Метка успешно удалена<', 'У вас нет меток'))
)


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

    def get_page(self, get_link, post_link=None, post_data=None):
        if post_link:
            self.client.post(post_link, post_data)
        response = self.client.get(get_link)
        return response.content.decode("utf-8")

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

        for prepear_data, cases in TEST_CASE:
            get_link, post_link, post_data = prepear_data
            content = self.get_page(get_link, post_link, post_data)
            for case in cases:
                self.assertTrue(content.__contains__(case))
