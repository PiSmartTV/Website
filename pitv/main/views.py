from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import CustomUserCreationForm, CustomAuthenticationForm

def home(request):
    return render(request, 'home.html', {'title': _('Home')})

def not_available(request):
    return render(request, 'not-available.html', {'title': _('Whoops')})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('pitv-home')
        else:
            print(form.errors.as_text)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form, 'title': _('Sign up')})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account logged in for {username}!')
            return redirect('pitv-home')
        else:
            print(form.errors.as_text)
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form, 'title': _('Log in')})