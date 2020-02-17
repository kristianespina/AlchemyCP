from django.contrib import admin
from django.urls import path, include, reverse_lazy

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('accounts/', views.home_view, name='home'),
    path('accounts/signup/', views.signup_view,name='signup'),
    path('accounts/logout/', views.logout_view,name='logout'),
    #path('accounts/login', views.signin),
    path('accounts/profile/', views.profile_view,name='profile'),
    path('accounts/success/', views.success_view,name='success'),
    path('accounts/change-pass/',
    auth_views.PasswordChangeView.as_view(
        template_name='form_submit.html',
        success_url=reverse_lazy('login')
        ), name='change-pass')
]

