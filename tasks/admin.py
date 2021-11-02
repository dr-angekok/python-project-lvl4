from django.contrib import admin

# Register your models here.
from .models import Task, TaskStatus

admin.site.register(TaskStatus)
admin.site.register(Task)
