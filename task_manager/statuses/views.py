from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.tasks.models import Task

from .forms import StatusForm
from .models import TaskStatus


class StatusesView(generic.ListView):
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return TaskStatus.objects.all()


class StatusView(generic.DetailView):
    model = TaskStatus
    template_name = "statuses/status.html"


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
    template_name = 'statuses/status_update.html'
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

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StatusDelete, self).delete(request, *args, **kwargs)
