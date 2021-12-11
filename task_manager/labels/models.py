from django.db import models
from django.urls import reverse


class TaskLabel(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('label', args=[str(self.id)])
