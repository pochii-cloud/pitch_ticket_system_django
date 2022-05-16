from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views import View

from core.forms import RegisterUserForm


class RegisterUser(View):
    def get(self, request):
        form = RegisterUserForm(request.POST)
        return render(request, 'Register.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'account created successfully')
        return render(request, 'Register.html', {'form': form})
