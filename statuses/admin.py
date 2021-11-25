from django.contrib import admin

# Register your models here.
from .models import TaskStatus

admin.site.register(TaskStatus)
