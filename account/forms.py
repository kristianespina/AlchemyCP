from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Login

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Login
        fields = ('username', 'sex', 'email', 'birthdate') 