from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tasks.filters import TaskFilter
from tasks.models import Task, TaskLable, TaskStatus
from tasks.forms import StatusForm, LableForm


class StatusesView(generic.ListView):
    template_name = 'tasks/statuses.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return TaskStatus.objects.all()

class StatusView(generic.DetailView):
    model = TaskStatus
    template_name = "tasks/status.html"

class StatusCreate(LoginRequiredMixin, CreateView):
    model = TaskStatus
    success_url = reverse_lazy('statuses')
    form_class = StatusForm

    def get_context_data(self, **kwargs):
        context = super(StatusCreate, self).get_context_data(**kwargs)
        context['statuses'] = TaskStatus.objects.all()
        return context

class StatusUpdate(LoginRequiredMixin, UpdateView):
    model = TaskStatus
    success_url = reverse_lazy('statuses')
    template_name = 'tasks/status_update.html'
    form_class = StatusForm

    def get_context_data(self, **kwargs):
        context = super(StatusUpdate, self).get_context_data(**kwargs)
        context['statuses'] = TaskStatus.objects.all()
        return context

class StatusDelete(LoginRequiredMixin, DeleteView):
    model = TaskStatus
    success_url = reverse_lazy('statuses')

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


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('name', 'content', 'assigned_to', 'status', 'lables')
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('name', 'content', 'assigned_to', 'status', 'lables')
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TaskUpdate, self).form_valid(form)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

    def get(self, request, pk):
        task = Task.objects.filter(pk=pk)
        if not task.filter(creator__id=request.user.id):
            messages.info(request, _('You do not have permission to delet another user task.'))
            return HttpResponseRedirect(self.success_url)
        return super().get(request, pk)


class LablesView(generic.ListView):
    template_name = 'tasks/lables.html'
    context_object_name = 'lables'

    def get_queryset(self):
        return TaskLable.objects.all()


class LableView(generic.DetailView):
    model = TaskLable
    template_name = "tasks/lable.html"


class LableCreate(LoginRequiredMixin, CreateView):
    model = TaskLable
    form_class = LableForm
    success_url = reverse_lazy('lables')

    def get_context_data(self, **kwargs):
        context = super(LableCreate, self).get_context_data(**kwargs)
        context['lables'] = TaskLable.objects.all()
        return context


class LableUpdate(LoginRequiredMixin, UpdateView):
    model = TaskLable
    form_class = LableForm
    success_url = reverse_lazy('lables')
    template_name = 'tasks/lable_update.html'

    def get_context_data(self, **kwargs):
        context = super(LableUpdate, self).get_context_data(**kwargs)
        context['lables'] = TaskLable.objects.all()
        return context


class LableDelete(LoginRequiredMixin, DeleteView):
    model = TaskLable
    success_url = reverse_lazy('lables')
