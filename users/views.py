from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from tasks.models import Task

from .forms import CustomUserCreationForm, UpdateUserForm


class Create(CreateView):
    template_name = 'users/create.html'

    def get(self, request):
        return render(request, self.template_name, context={'form': CustomUserCreationForm()})

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _('User registered successfully'))
            return redirect("/login")
        return render(request, self.template_name, context={'form': CustomUserCreationForm(data=request.POST)})


class Update(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = UpdateUserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.info(self.request, _('User edited successfully'))
        return redirect('/users')
 
    def dispatch(self, request, pk, *args, **kwargs):
        if request.user.id is not pk:
            if request.user.is_authenticated:
                messages.info(request, _('You do not have permission to modify another user.'))
                return redirect('/users')
            messages.info(request, _('You are not authorized! Please sign in.'))
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)


class Delete(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'users/delete.html'

    def get(self, request, user_id):
        context = {'user': User.objects.get(id=user_id)}
        return render(request, self.template_name, context=context)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        messages.info(request, _('Successfully delete.'))
        return redirect('/users')
    
    def dispatch(self, request, user_id, *args, **kwargs):
        if request.user.id is not user_id:
            if request.user.is_authenticated:
                messages.info(request, _('You do not have permission to modify another user.'))
                return redirect('/users')
            messages.info(request, _('You are not authorized! Please sign in.'))
            return redirect('/login')
        if Task.objects.filter(creator__id=user_id) or Task.objects.filter(assigned_to__id=user_id):
            messages.info(request, _('It is impossible to delete a user who has tasks.'))
            return redirect('/users')
        return super().dispatch(request, user_id, *args, **kwargs)


class List(View):
    template_name = 'users/list.html'

    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, self.template_name, context=context)


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_url = '/'
    success_message = _("You are now logged in.")


def logged_out_message(sender, user, request, **kwargs):
    messages.info(request, _('You are now logged out.'))

user_logged_out.connect(logged_out_message)
