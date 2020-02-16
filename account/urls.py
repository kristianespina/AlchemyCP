from django.contrib import admin
from django.urls import path, include, reverse_lazy

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('accounts/signup/', views.signup),
    #path('accounts/login', views.signin),
    path('accounts/profile/', views.profile),
    path('accounts/success/', views.success),
    path('accounts/changepass/',
    auth_views.PasswordChangeView.as_view(
        template_name='password_change.html',
        success_url=reverse_lazy('login')
        ), name='password_change')
]

