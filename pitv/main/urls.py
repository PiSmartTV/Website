from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='pitv-home'),
    path('signup/', views.signup, name='pitv-signup'),
    path('not-available/', views.not_available, name='pitv-not-available'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='pitv-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='pitv-logout')
]
