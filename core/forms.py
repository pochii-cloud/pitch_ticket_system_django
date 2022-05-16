from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.models import Fixture


class AddFixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['TeamA', 'TeamB', 'Date', 'Time', 'Ground']
        # widgets = {
        #     'TeamA': forms.TextInput(attrs={'class': 'form-control'}),
        #     'TeamB': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Date': forms.DateInput(attrs={'class': 'form-control'}),
        #     'Time': forms.TimeInput(attrs={'class': 'form-control'}),
        #     'Ground': forms.TextInput(attrs={'class': 'form-control'}),
        # }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'Password1': forms.PasswordInput(),
        #     'Password2': forms.PasswordInput(),
        # }
