from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tasks.filters import TaskFilter

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