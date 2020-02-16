from django.shortcuts import render

#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from .forms import SignUpForm, SignInForm
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

"""
def signin(request):
    login_form = SignInForm(request.POST)
    
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            last_login = user.last_login
            login(request, user)
        else:
            login_form.add_error(None, "Your account is inactive.")
    print(login_form.is_valid())
    return render(request, 'login.html', {'form': login_form}) 
"""
def profile(request):
    return render(request, 'profile.html')

def success(request):
    return render(request, 'success.html')