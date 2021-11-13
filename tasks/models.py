from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



class TaskLable(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lable', args=[str(self.id)])

class TaskStatus(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_status', args=[str(self.id)])

class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=600)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, null=False, blank=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name="assigned_to")
    lables = models.ManyToManyField(TaskLable, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task', args=[str(self.id)])

class RelatedModel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(TaskLable, on_delete=models.PROTECT)
