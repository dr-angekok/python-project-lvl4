from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.mixins import NonUseItemRequireMixin

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


class StatusDelete(LoginRequiredMixin, SuccessMessageMixin, NonUseItemRequireMixin, DeleteView):
    model = TaskStatus
    success_url = reverse_lazy('statuses')
    success_message = _("Status successfully deleted")
    home_link = '/statuses'
    delete_deny_massage = _('Unable to delete status because it is in use')
    non_use_require_field = 'status'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StatusDelete, self).delete(request, *args, **kwargs)
