from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='pitv-home'),
    path('signup/', views.signup, name='pitv-signup'),
    path('not-available/', views.not_available, name='pitv-not-available')
]
