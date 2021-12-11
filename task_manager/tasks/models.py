from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from task_manager.labels.models import TaskLabel
from task_manager.statuses.models import TaskStatus


class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=600)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, null=False, blank=False)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 related_name='executor')
    labels = models.ManyToManyField(TaskLabel, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task', args=[str(self.id)])


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(TaskLabel, on_delete=models.PROTECT)
