from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from .models import User1page, User2page
from django.views.generic import View, ListView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
import pyotp

from .forms import UserLoginForm
from django.contrib.auth import login, logout

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Отрисовка HTML-шаблона index.html с данными внутри
    return render(request, 'index.html', context={})

class User1page(LoginRequiredMixin, View):
    model = User1page
    template = 'templates/User1page.html'
    #raise_exception = True
    def get(self, request):
        current_user = request.user
        if not request.user.groups.filter(name='Users1group'):
            return redirect('/authsys1app/')
        else:
            return render(request, 'User1page.html', context={'id': current_user.id}) # Отрисовка HTML-шаблона с данными внутри

class User2page(View):
    model = User2page
    template = 'User2page.html'
    def get(self, request):
        current_user = request.user
        if not request.user.groups.filter(name='Users2group'):
            return redirect('/authsys1app/')
        else:
            return render(request, 'User2page.html', context={'id': current_user.id}) # Отрисовка HTML-шаблона с данными внутри

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')