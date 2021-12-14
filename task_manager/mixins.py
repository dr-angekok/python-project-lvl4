from django.contrib import messages
from django.utils.translation import ugettext as _
from django.shortcuts import redirect
from task_manager.tasks.models import Task


class PermissionRequiredMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        if request.user.id is not pk:
            if request.user.is_authenticated:
                messages.info(request, self.modify_deny_message)
                return redirect(self.home_link)
            messages.info(request, _('You are not authorized! Please sign in.'))
            return redirect('/login')
        return super().dispatch(request, pk, *args, **kwargs)


class UserNotInvolvedMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        if Task.objects.filter(creator__id=pk) or Task.objects.filter(executor__id=pk):
            messages.info(request, self.delete_deny_massage)
            return redirect('/users')
        return super().dispatch(request, pk, *args, **kwargs)


class NonUseItemRequireMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        filter_args = {'{}__id'.format(self.non_use_require_field): pk}
        if Task.objects.filter(**filter_args):
            messages.info(request, self.delete_deny_massage)
            return redirect(self.home_link)
        return super().dispatch(request, pk, *args, **kwargs)


class GetContextDataMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_fild_name] = self.context_objects_model.objects.all()
        return context
