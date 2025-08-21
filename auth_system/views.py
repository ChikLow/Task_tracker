from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from auth_system.forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class UserCreateView(CreateView):
    model = User
    template_name = 'auth_system/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('task_list')


class UserLoginView(LoginView):
    template_name = 'auth_system/login.html'
    form_class = LoginForm