from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tasks.filters import TaskFilter
from tasks.forms import TaskForm
from tasks.models import Task


class TasksView(generic.ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(
            self.request.GET,
            queryset=self.get_queryset(),)
        return context

    def get_queryset(self):
        if self.request.GET:
            parameters = self.request.GET
            filters = {}
            for key, value in parameters.items():
                if value:
                    filters[key] = value
            return Task.objects.filter(**filters)
        return Task.objects.all()


class TaskView(generic.DetailView):
    model = Task
    template_name = "tasks/task.html"
    success_url = reverse_lazy('tasks')


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = "tasks/task_create_form.html"
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully Created")
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    template_name = "tasks/task_update_form.html"
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully updated")
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TaskUpdate, self).form_valid(form)


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully deleted")

    def get(self, request, pk):
        task = Task.objects.filter(pk=pk)
        if not task.filter(creator__id=request.user.id):
            messages.info(request, _('You do not have permission to delet another user task.'))
            return HttpResponseRedirect(self.success_url)
        return super().get(request, pk)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDelete, self).delete(request, *args, **kwargs)
