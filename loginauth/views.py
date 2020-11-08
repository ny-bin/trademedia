from django.shortcuts import render

# ここから追加
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm

# Create your views here.
from django.http import HttpResponse

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'loginauth/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'loginauth/login.html'
# ここまで追加

class Create_User():
    pass