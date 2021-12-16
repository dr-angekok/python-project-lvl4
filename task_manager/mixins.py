from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

from task_manager.tasks.models import Task


class PermissionRequiredMixin():
    """Adds the ability to check if the user is the one being edited.
    Required:
            modify_deny_message: The message of the impossibility of editing.
            home_link: Link to the site to redirect if the user does not match the current one
    """

    def dispatch(self, request, pk, *args, **kwargs):
        if request.user.id is not pk:
            if request.user.is_authenticated:
                messages.info(request, self.modify_deny_message)
                return redirect(self.home_link)
            messages.info(request, _('You are not authorized! Please sign in.'))
            return redirect('/login')
        return super().dispatch(request, pk, *args, **kwargs)


class UserNotInvolvedMixin():
    """Checks if the user has active tasks for himself or for others and,
    if there are any, aborts the operation.
    Required:
            delete_deny_massage: The message of the impossibility of delete.
    """

    def dispatch(self, request, pk, *args, **kwargs):
        if Task.objects.filter(creator__id=pk) or Task.objects.filter(executor__id=pk):
            messages.info(request, self.delete_deny_massage)
            return redirect('/users')
        return super().dispatch(request, pk, *args, **kwargs)


class NonUseItemRequireMixin():
    """Checks if a value is used in tasks and aborts if used.
    Required:
            delete_deny_massage: The message of the impossibility of delete.
            non_use_require_field: The field in the model whose value should not be used
            home_link: Failure redirect link.
    """
    def dispatch(self, request, pk, *args, **kwargs):
        filter_args = {'{}__id'.format(self.non_use_require_field): pk}
        if Task.objects.filter(**filter_args):
            messages.info(request, self.delete_deny_massage)
            return redirect(self.home_link)
        return super().dispatch(request, pk, *args, **kwargs)


class GetContextDataMixin():
    """Provides context for filling out a form field.
    Required:
            context_fild_name: Model field name for context.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_fild_name] = self.context_objects_model.objects.all()
        return context


class OnDeleteMessageMixin():
    """Same as SuccessMessageMixin but when delete via standard form."""

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class FilterViewsSetMixin():
    """Creates a context for the form, applying the filter that exists on the form."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset_class(
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
            return self.model.objects.filter(**filters)
        return self.model.objects.all()


class AddCreatorAsCurrentUserMixin():
    """Fill the 'creator' field with the current user"""

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
