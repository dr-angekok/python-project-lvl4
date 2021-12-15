from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.mixins import (AddCreatorAsCurrentUserMixin,
                                 FilterViewsSetMixin, OnDeleteMessageMixin)

from .filters import TaskFilter
from .forms import TaskForm
from .models import Task


class TasksView(FilterViewsSetMixin, generic.ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks_list'
    filterset_class = TaskFilter


class TaskView(generic.DetailView):
    model = Task
    template_name = "tasks/task.html"
    success_url = reverse_lazy('tasks')


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, AddCreatorAsCurrentUserMixin, CreateView):
    model = Task
    template_name = "tasks/task_create_form.html"
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully Created")
    form_class = TaskForm


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, AddCreatorAsCurrentUserMixin, UpdateView):
    model = Task
    template_name = "tasks/task_update_form.html"
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully updated")
    form_class = TaskForm


class TaskDelete(LoginRequiredMixin, OnDeleteMessageMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully deleted")
    delete_deny_massage = _('You do not have permission to delet another user task.')

    def get(self, request, pk):
        task = Task.objects.filter(pk=pk)
        if not task.filter(creator__id=request.user.id):
            messages.info(request, self.delete_deny_massage)
            return HttpResponseRedirect(self.success_url)
        return super().get(request, pk)
