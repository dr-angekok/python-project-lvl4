from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic.edit import UpdateView


class Create(View):
    template_name = 'users/create.html'

    def get(self, request):
        return render(request, self.template_name, context={'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _('You are now logged in.'))
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("/")
        else:
            return render(request, self.template_name, context={'form': form})


class Update(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'password')
    template_name = 'users/update.html'
    success_url = '/users/'


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

user_logged_in.connect(logged_in_message)