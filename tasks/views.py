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
from tasks.forms import LableForm, StatusForm
from tasks.models import Task, TaskLable, TaskStatus


class StatusesView(generic.ListView):
    template_name = 'tasks/statuses.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return TaskStatus.objects.all()

class StatusView(generic.DetailView):
    model = TaskStatus
    template_name = "tasks/status.html"

class StatusCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TaskStatus
    success_url = reverse_lazy('statuses')
    form_class = StatusForm
    success_message = _("Status successfully created")

    def get_context_data(self, **kwargs):
        context = super(StatusCreate, self).get_context_data(**kwargs)
        context['statuses'] = TaskStatus.objects.all()
        return context

class StatusUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TaskStatus
    success_url = reverse_lazy('statuses')
    template_name = 'tasks/status_update.html'
    form_class = StatusForm
    success_message = _("Status successfully updated")

    def get_context_data(self, **kwargs):
        context = super(StatusUpdate, self).get_context_data(**kwargs)
        context['statuses'] = TaskStatus.objects.all()
        return context

class StatusDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TaskStatus
    success_url = reverse_lazy('statuses')
    success_message = _("Status successfully deleted")

    def dispatch(self, request, pk, *args, **kwargs):
        if Task.objects.filter(status__id=pk):
            messages.info(request, _('Unable to delete status because it is in use'))
            return redirect('/statuses')
        return super().dispatch(request, pk, *args, **kwargs)

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
    fields = ('name', 'content', 'assigned_to', 'status', 'lables')
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully Created")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ('name', 'content', 'assigned_to', 'status', 'lables')
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully updated")
    
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


class LablesView(generic.ListView):
    template_name = 'tasks/lables.html'
    context_object_name = 'lables'

    def get_queryset(self):
        return TaskLable.objects.all()


class LableView(generic.DetailView):
    model = TaskLable
    template_name = "tasks/lable.html"


class LableCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TaskLable
    form_class = LableForm
    success_url = reverse_lazy('lables')
    success_message = _("Lable successfully Created")

    def get_context_data(self, **kwargs):
        context = super(LableCreate, self).get_context_data(**kwargs)
        context['lables'] = TaskLable.objects.all()
        return context


class LableUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TaskLable
    form_class = LableForm
    success_url = reverse_lazy('lables')
    template_name = 'tasks/lable_update.html'
    success_message = _("Lable successfully updated")

    def get_context_data(self, **kwargs):
        context = super(LableUpdate, self).get_context_data(**kwargs)
        context['lables'] = TaskLable.objects.all()
        return context


class LableDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TaskLable
    success_url = reverse_lazy('lables')
    success_message = _("Lable successfully deleted")
    
    def dispatch(self, request, pk, *args, **kwargs):
        if Task.objects.filter(status__id=pk):
            messages.info(request, _('Unable to delete lable because it is in use'))
            return redirect('/lables')
        return super().dispatch(request, pk, *args, **kwargs)

