from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        # Create and save database object from the data bound to the form
        # See https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
        user = form.save()
        user.refresh_from_db()
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})