from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tasks.models import Task, TaskStatus, TaskLable


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
    fields = '__all__'
    success_url = reverse_lazy('statuses')

    def get_context_data(self, **kwargs):
        context = super(StatusCreate, self).get_context_data(**kwargs)
        context['statuses'] = TaskStatus.objects.all()
        return context

class StatusUpdate(LoginRequiredMixin, UpdateView):
    model = TaskStatus
    fields = '__all__'
    success_url = reverse_lazy('statuses')
    template_name = 'tasks/status_update.html'

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
        return context


class TaskView(generic.DetailView):
    model = Task
    template_name = "tasks/task.html"
    success_url = reverse_lazy('tasks')


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    def get_initial(self, *args, **kwargs):
        initial = super(TaskCreate, self).get_initial(**kwargs)
        initial['creator'] = self.request.user
        return initial


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')


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
    fields = '__all__'
    success_url = reverse_lazy('lables')

    def get_context_data(self, **kwargs):
        context = super(LableCreate, self).get_context_data(**kwargs)
        context['lables'] = TaskLable.objects.all()
        return context


class LableUpdate(LoginRequiredMixin, UpdateView):
    model = TaskLable
    fields = '__all__'
    success_url = reverse_lazy('lables')
    template_name = 'tasks/lable_update.html'

    def get_context_data(self, **kwargs):
        context = super(LableUpdate, self).get_context_data(**kwargs)
        context['lables'] = TaskLable.objects.all()
        return context


class LableDelete(LoginRequiredMixin, DeleteView):
    model = TaskLable
    success_url = reverse_lazy('lables')