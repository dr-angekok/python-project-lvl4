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

