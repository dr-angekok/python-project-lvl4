from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class TaskStatus(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a status name")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_status', args=[str(self.id)])

class Task(models.Model):
    name = models.CharField(max_length=255, help_text="Task name.")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(
        max_length=600,
        help_text="Enter a task")
    status = models.ForeignKey(
        TaskStatus,
        on_delete=models.CASCADE,
        null=False, blank=False)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_to")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task', args=[str(self.id)])
