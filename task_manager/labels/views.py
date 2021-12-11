from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.mixins import NonUseItemRequireMixin

from .forms import LabelForm
from .models import TaskLabel


class LabelsView(generic.ListView):
    template_name = 'labels/labels.html'
    context_object_name = 'labels'

    def get_queryset(self):
        return TaskLabel.objects.all()


class LabelView(generic.DetailView):
    model = TaskLabel
    template_name = "labels/label.html"


class LabelCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TaskLabel
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _("Label successfully Created")

    def get_context_data(self, **kwargs):
        context = super(LabelCreate, self).get_context_data(**kwargs)
        context['labels'] = TaskLabel.objects.all()
        return context


class LabelUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TaskLabel
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    template_name = 'labels/label_update.html'
    success_message = _("Label successfully updated")

    def get_context_data(self, **kwargs):
        context = super(LabelUpdate, self).get_context_data(**kwargs)
        context['labels'] = TaskLabel.objects.all()
        return context


class LabelDelete(LoginRequiredMixin, SuccessMessageMixin, NonUseItemRequireMixin, DeleteView):
    model = TaskLabel
    success_url = reverse_lazy('labels')
    success_message = _("Label successfully deleted")
    home_link = '/labels'
    delete_deny_massage = _('Unable to delete label because it is in use')
    non_use_require_field = 'labels'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(LabelDelete, self).delete(request, *args, **kwargs)
