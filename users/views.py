from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic.edit import UpdateView, CreateView
from .forms import UpdateUserForm, CustomUserCreationForm

class Create(CreateView):
    template_name = 'users/create.html'

    def get(self, request):
        return render(request, self.template_name, context={'form': CustomUserCreationForm()})

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("/")
        else:
            return render(request, self.template_name, context={'form': CustomUserCreationForm()})


class Update(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = UpdateUserForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('/users')
 
    def dispatch(self, request, pk, *args, **kwargs):
        if request.user.id is not pk:
            messages.info(request, _('You do not have permission to modify another user.'))
            return redirect('/users')
        else:
            return super().dispatch(request, *args, **kwargs)


class Delete(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'users/delete.html'

    def get(self, request, user_id):
        context = {'user': User.objects.get(id=user_id)}
        if request.user.id is not user_id:
            messages.info(request, _('You do not have permission to modify another user.'))
            return redirect('/users')
        else:
            return render(request, self.template_name, context=context)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        messages.info(request, _('Successfully delete.'))
        return redirect('/')


class List(View):
    template_name = 'users/list.html'

    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, self.template_name, context=context)


def logged_in_message(sender, user, request, **kwargs):
    messages.info(request, _('You are now logged in.'))


def logged_out_message(sender, user, request, **kwargs):
    messages.info(request, _('You are now logged out.'))

user_logged_in.connect(logged_in_message)
user_logged_out.connect(logged_out_message)
