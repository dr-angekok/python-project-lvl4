from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.translation import ugettext as _


def index(request):
    return render(request, 'index.html')


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_url = '/'
    success_message = _('You are now logged in.')


class LogoutFormView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are now logged out.'))
        return super().dispatch(request, *args, **kwargs)
