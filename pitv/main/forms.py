from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.utils.translation import gettext as _


class CustomUserCreationForm(UserCreationForm):
    input_attrs = {'class': 'form-control', 'placeholder': _('E-Mail Address')}

    email = forms.EmailField(widget=forms.TextInput(attrs=input_attrs))

    input_attrs['placeholder'] = _('First Name')
    first_name = forms.CharField(widget=forms.TextInput(attrs=input_attrs))

    input_attrs['placeholder'] = _('Last Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs=input_attrs))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Password')})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Confirm password')})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Username')})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Password')})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Username')})

    class Meta:
        model = User
        fields = ['username', 'password']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Old password')})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('New password')})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Confirm new password')})

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
