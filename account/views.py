from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from core.forms import RegisterUserForm


class RegisterUser(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'Register.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'account created successfully')
            return redirect('LoginPage')
        return render(request, 'Register.html', {'form': form})


class LoginPage(LoginView):
    template_name = 'LoginPage.html'


class AdminLogin(LoginView):
    template_name = 'AdminLogin.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return HttpResponse('you are not allowed to access this page')
        elif self.request.user.is_superuser and self.request.user.is_superuser:
            return redirect('AdminPage')


class LogoutPage(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('LoginPage')
