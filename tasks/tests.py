from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from labels.models import TaskLabel
from statuses.models import TaskStatus

from tasks import views
from tasks.models import Task


TEST_CASE = (
    (('/tasks/', '/login/',
      {'username': 'Igor', 'password': 'password!@#$123'}), ('Task name',)),
    (('/tasks/1/', None,
      None), ('Task name', 'Task description')),
    (('/tasks/', '/tasks/1/delete/',
      None), ('"success">Задача успешно удалена<', 'Нет задач'))
)


class TaskTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Igor',
            password='password!@#$123',
        )
        self.client = Client()

    def createTask(self):
        status = TaskStatus.objects.create(name='Any status')
        label = TaskLabel.objects.create(name='Any label')
        task = Task.objects.create(
            name='Task name',
            description='Task description',
            creator=self.user,
            executor=self.user,
            status=status)
        task.labels.add(label)
        return task

    def get_page(self, get_link, post_link=None, post_data=None):
        if post_link:
            self.client.post(post_link, post_data)
        response = self.client.get(get_link)
        return response.content.decode("utf-8")

    def test_task_create(self):
        task = self.createTask()
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(Task.objects.count(), 1)

    def test_tasks_view(self):
        self.createTask()
        request = self.factory.get('/tasks/')
        request.user = self.user
        response = views.TasksView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        for prepear_data, cases in TEST_CASE:
            get_link, post_link, post_data = prepear_data
            content = self.get_page(get_link, post_link, post_data)
            for case in cases:
                self.assertTrue(content.__contains__(case))
