from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import LoginForm
from .forms import UserCreateForm
from .models import User

# Create your views here.
from django.http import HttpResponse

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'loginauth/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'loginauth/login.html'

class Create_user(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('user_name')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, User)
            return redirect('/')
        return render(request, 'create_user.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'create_user.html', {'form': form,})


