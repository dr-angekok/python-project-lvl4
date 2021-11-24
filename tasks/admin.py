from django.contrib import admin

# Register your models here.
from .models import Task, TaskStatus, TaskLabel

admin.site.register(TaskStatus)
admin.site.register(Task)
admin.site.register(TaskLabel)
