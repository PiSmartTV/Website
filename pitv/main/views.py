from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})