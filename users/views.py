from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin


class Create(View, SuccessMessageMixin):
    template_name = "users/create.html"
    success_message = 'Успешно.'

    def get(self, request):
        return render(request, self.template_name, context={"form": UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, self.template_name, context={"form": form})


class Update(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    fields = ('username', 'first_name', 'last_name', 'password')
    template_name = 'users/update.html'
    success_url = "/users/"
    success_message = 'Успешно отредактирован.'


class Delete(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "users/delete.html"

    def get(self, request, user_id):
        context = {"user": User.objects.get(id=user_id)}
        return render(request, self.template_name, context=context)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect("/users/")


class List(View):
    template_name = "users/list.html"

    def get(self, request):
        users = User.objects.all()
        context = {"users": users}
        return render(request, self.template_name, context=context)

