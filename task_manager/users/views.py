from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from task_manager.mixins import PermissionRequiredMixin, UserNotInvolvedMixin

from .forms import UserForm


class Create(CreateView):
    template_name = 'users/create.html'

    def get(self, request):
        return render(request, self.template_name, context={'form': UserForm()})

    def post(self, request):
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _('User registered successfully'))
            return redirect("/login")
        return render(request,
                      self.template_name,
                      context={'form': UserForm(data=request.POST)})


class Update(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = UserForm
    home_link = '/users'
    modify_deny_message = _('You do not have permission to modify another user.')
    success_message = _('User edited successfully')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.info(self.request, self.success_message)
        return redirect(self.home_link)


class Delete(LoginRequiredMixin, PermissionRequiredMixin, UserNotInvolvedMixin, View):
    login_url = 'login'
    template_name = 'users/delete.html'
    home_link = '/users'
    modify_deny_message = _('You do not have permission to delete another user.')
    delete_deny_massage = _('It is impossible to delete a user who has tasks.')
    success_message = _('Successfully delete.')

    def get(self, request, user_id):
        context = {'user': User.objects.get(id=user_id)}
        return render(request, self.template_name, context=context)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        messages.info(request, self.success_message)
        return redirect(self.home_link)


class List(View):
    template_name = 'users/list.html'

    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, self.template_name, context=context)
