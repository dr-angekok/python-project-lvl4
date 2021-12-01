from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from labels.models import TaskLabel
from statuses.models import TaskStatus

from tasks import views
from tasks.models import Task


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
        response = self.client.post('/login/', {'username': 'Igor', 'password': 'password!@#$123'})
        response = self.client.get('/tasks/')
        content = response.content.decode("utf-8")
        self.assertTrue(content.__contains__('Task name'))
