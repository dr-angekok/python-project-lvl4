from django.contrib import admin

# Register your models here.
from .models import TaskLabel

admin.site.register(TaskLabel)
