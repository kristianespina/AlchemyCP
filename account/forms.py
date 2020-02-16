from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from .models import Login

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Login
        fields = ('username', 'sex', 'email', 'birthdate') 

class SignInForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = Login