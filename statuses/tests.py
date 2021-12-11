from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from statuses import views
from statuses.models import TaskStatus


TEST_CASE = (
    (('/statuses/', '/login/',
      {'username': 'Igor', 'password': 'password!@#$123'}), ('Any status',)),
    (('/statuses/1/', None,
      None), ('Any status')),
    (('/statuses/', '/statuses/1/update/',
      {'name': 'Changed status', }), ('Changed status', '"success">Статус успешно изменён<')),
    (('/statuses/', '/statuses/1/delete/',
      None), ('"success">Статус успешно удалён<', 'У вас нет статусов'))
)


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

    def get_page(self, get_link, post_link=None, post_data=None):
        if post_link:
            self.client.post(post_link, post_data)
        response = self.client.get(get_link)
        return response.content.decode("utf-8")

    def test_status_view(self):
        self.createStatus()
        request = self.factory.get('/statuses/')
        request.user = self.user
        response = views.StatusesView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        for prepear_data, cases in TEST_CASE:
            get_link, post_link, post_data = prepear_data
            content = self.get_page(get_link, post_link, post_data)
            for case in cases:
                self.assertTrue(content.__contains__(case))
