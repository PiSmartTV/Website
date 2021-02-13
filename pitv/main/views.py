from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import CustomUserCreationForm, CustomAuthenticationForm

ACCOUNT_FIELDS = [_('Devices')]

def home(request):
    return render(request, 'home.html', {'title': _('Home')})

def not_available(request):
    return render(request, 'not-available.html', {'title': _('Whoops')})

def account_devices(request):
    return render(request, 'account/devices.html', {'title': _('Devices'), 'fields': ACCOUNT_FIELDS})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('pitv-home')
        else:
            print(form.errors.as_data())
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form, 'title': _('Sign up')})

def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('pitv-home')
            else:
                print('User not found')

            
            messages.success(request, f'Account logged in for {username}!')
            return redirect('pitv-home')
        else:
            print(form.errors.as_data())
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form, 'title': _('Log in')})