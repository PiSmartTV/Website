from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from user_sessions.models import Session
from user_sessions.views import SessionDeleteView

from .models import DeviceCode
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm

ACCOUNT_FIELDS = [_('Devices'), _('Edit'), _('Logout')]


def home(request):
    return render(request, 'home.html', {'title': _('Home')})


def not_available(request):
    return render(request, 'not-available.html', {'title': _('Whoops')})

@login_required
def account_edit(request):
    if request.method == 'POST' :
        form = CustomPasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data.get('new_password2'))
            user.save()

            login(request, user=user)

            messages.success(request, 'Password changed successfully!')
            return redirect('pitv-edit')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(
        request,
        'account/edit.html',
        {
            'form': form,
            'title': _('Edit'),
            'fields': ACCOUNT_FIELDS
        }
    )

@login_required
def account_devices(request):
    if request.method == 'GET':

        devices = Session.objects.filter(user=request.user)

        return render(
            request,
            'account/devices.html',
            {
                'title': _('Devices'),
                'fields': ACCOUNT_FIELDS,
                'devices': devices
            }
        )

    elif request.method == 'POST':
        code = request.POST.get('code')

        if code:
            device_code = DeviceCode.objects.filter(code=code).first()

            if device_code:
                device_code.approved_user = request.user
                device_code.save()

                messages.success(request, 'Successfully registered a new device!')

                return redirect('pitv-devices')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, _(f'Account created for {username}!'))
            return redirect('pitv-home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form, 'title': _('Sign up')})


# TODO: Add redirect to next parameter
def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, _(f'Successfully logged in as {username}!'))
                login(request, user)
                return redirect('pitv-home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form, 'title': _('Log in')})


class CustomSessionDeleteView(SessionDeleteView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def get_success_url(self):
        return str(reverse_lazy('pitv-account'))