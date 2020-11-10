from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from loginauth.forms import LoginForm
from .models import User
from .forms import UserCreateForm

# Create your views here.
from django.http import HttpResponse

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'loginauth/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'loginauth/login.html'

def signup(request):
    if request.method == 'POST':
        # user.username = request.POST["user_name"]
        form = UserCreateForm(request.POST)
        print(request.POST["username"])
        # form.password1 = request.POST["password1"]
        # form.password2 = request.POST["password2"]
        if form.is_valid():
            print("検証に成功しました。データを保存します")
            form.save()
        else:
            print("検証に失敗したので、データを保存しません。検証に失敗した理由を次に表示します。")
            print(form.errors)
        # user = form.save()
        # login(request, user)
        # return redirect('/login')
    # else:
    #     form = UserCreationForm(User)
    return render(request, 'loginauth/create_user.html')


